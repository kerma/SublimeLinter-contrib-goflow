import os
import os.path
import sublime

from SublimeLinter.lint import Linter
from SublimeLinter.lint.linter import LintMatch
from SublimeLinter.lint.linter import get_view_context


class GoFmt(Linter):

    defaults = {'selector': 'source.go'}
    cmd = ['gofmt', '-w', '${file}']
    tempfile_suffix = '-'
    regexp = r'.*'


class GoTest(Linter):

    defaults = {'selector': 'source.go'}
    cmd = ['go', 'test']
    tempfile_suffix = '-'
    regex = (r'.+[\d\w]+_test.go:(?P<line>\d+):\s*(?P<message>.*)'
             '|--- (?P<error>FAIL): (?P<near>.+) \(.*')

    def run(self, cmd, code):
        filename = os.path.basename(self.filename)
        if filename.endswith("_test.go"):
            return self.communicate(cmd, code="")

    # overrides the one in SublimeLinter to disable auto_append
    def communicate(self, cmd, code=None):
        """Run an external executable using stdin to pass code and return its output."""
        ctx = get_view_context(self.view)
        ctx['file_on_disk'] = self.filename

        cmd = self.finalize_cmd(
            cmd, ctx, at_value=self.filename, auto_append=False)
        return self._communicate(cmd, None)

    def split_match(self, match):
        """Override for SublimeLinter split_match to provide find
        the correct test name to highlight.
        """

        lintmatch = super().split_match(match)
        if lintmatch.error != 'FAIL':
            return lintmatch

        # find the test definition and "make it red"
        content = self.view.substr(sublime.Region(0, self.view.size()))
        begin = content.find("func " + lintmatch.near)
        row, col = self.view.rowcol(begin + 5)
        return LintMatch(
            match=lintmatch.match,
            line=row,
            col=col,
            message=lintmatch.error)
