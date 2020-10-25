# TODO

## Next step

    * update lab guides for Python language
    * fix running GUI apps (issue with importing package)

## Improvements

    * test project on Windows

    - testing
      - enable appveyor testing?
      - enable macOS testing on Travis CI
    - cleaning
      - use fresher versions of dependencies (do we need everything from requirements?)
      - fix flake8 warning (newer version of flake8 and/or pycodestyle=2.4+)
    - guides
        - test links in the MD files
        - add TOC to files
    - change license to MIT or something like that
    - implement one more topic as an excersize

## Quickstart guide

  $ pyenv uninstall 3.7.3
  $ env   PATH="$(brew --prefix tcl-tk)/bin:$PATH"   LDFLAGS="-L$(brew --prefix tcl-tk)/lib"   CPPFLAGS="-I$(brew --prefix tcl-tk)/include"   PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"   CFLAGS="-I$(brew --prefix tcl-tk)/include"   PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'"   pyenv install 3.7.3
  $ pyenv versions
  $ pyenv global 3.7.3
  $ python -V
  $ python -m tkinter -c 'tkinter._test()'
  $ python -m venv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  $ nosetests -x --with-coverage code/*
  $ flake8 --max-line-length=110 code

## Notes

pyenv
    - https://opensource.com/article/19/5/python-3-default-mac

Installing tkinter on macOS

    - https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos/60469203#60469203
      - for me worked only after the homebrew reinstall
      - also helpful for details: https://github.com/pyenv/pyenv/issues/1375#issuecomment-589964703, https://blog.lanzani.nl/2020/install-tkinter-macos/

Python virtual environment

    $ python -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    # WORK HERE
    $ deactivate # when needed

PIP

    $ sudo easy_install pip
    $ pip3 install flake8== # list available versions of the package
