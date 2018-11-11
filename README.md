SublimeLinter-contrib-goflow
============================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-__linter__.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-__linter__)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to `go fmt` and `go test`. It will be used with files that have the “source.go” syntax.

It's pretty much an abuse of the wonderful SublimeLinter framework to run `go fmt` and `go test` once you save a file.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use Git to install this plugin to Sublime Packages dir (eg: `~/Library/Application\ Support/Sublime Text 3/Packages`):

  ```
  $ git clone https://github.com/kerma/SublimeLinter-contrib-goflow.git
  ```

Before installing this plugin, you must ensure that `go` is installed on your system.

In order for `go` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

For Go vendoring to work properly it's wise to start Sublime from command line via `subl` command. 

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
