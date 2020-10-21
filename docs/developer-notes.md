# TODO

## Next step

      * update lab guides for Python language

## Improvements

    - must have
      * test project on Windows

    - nice to have
        - testing
          - enable macOS testing on Travis CI
          - enable appveyor testing?
        - cleaning
          - remove `src` folders, uplevel their contents
          - fix flake8 warning (newer version of flake8 and/or pycodestyle=2.4+)
          - remove log files in the end of the test (or create them in folder)
        - change license to MIT or something like that
        - implement one more topic as an excersize

## Notes

Install tkinter on macOS

    - resolve: ModuleNotFoundError: No module named 'Tkinter'
    - https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos/60469203#60469203
      - but only after the homebrew reinstall
      - also helpful for details: https://github.com/pyenv/pyenv/issues/1375#issuecomment-589964703

Python virtual environment

    $ python -m venv env
    $ source env/bin/activate
    $ deactivate # if needed

Dependencies installation

    $ easy_install pip
    $ sudo easy_install pip
    $ pip install -r requirements.txt

Random commands

    $ python -m pip install flake8
    $ PATH="/Users/kirill-personal/Library/Python/2.7/bin:$PATH"
    $ pip3 install flake8== # list available versions of the package

tkinter
    # https://blog.lanzani.nl/2020/install-tkinter-macos/
    $ brew install tcl-tk


useful reads
    - https://opensource.com/article/19/5/python-3-default-mac
    - https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos

==> Caveats
Commands also provided by macOS have been installed with the prefix "g".
If you need to use these commands with their normal names, you
can add a "gnubin" directory to your PATH from your bashrc like:
  PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

sudo chown -R $(whoami) $(brew --prefix)/*

quickstart

  606  pyenv uninstall 3.7.3
  607  env   PATH="$(brew --prefix tcl-tk)/bin:$PATH"   LDFLAGS="-L$(brew --prefix tcl-tk)/lib"   CPPFLAGS="-I$(brew --prefix tcl-tk)/include"   PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig"   CFLAGS="-I$(brew --prefix tcl-tk)/include"   PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'"   pyenv install 3.7.3
  608  pyenv versions
  609  pyenv global 3.7.3
  610  python -V
  611  python -m tkinter -c 'tkinter._test()'
  612  python -m venv env
  613  source env/bin/activate
  614  pip install -r requirements.txt
  615  nosetests -x --with-coverage code/*
  616  flake8 --max-line-length=110 code