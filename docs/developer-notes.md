# TODO

## Next step

    * test GUI
      - resolve: ModuleNotFoundError: No module named 'Tkinter'
      - https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos/60469203#60469203
        - but only after the homebrew reinstall
        - also helpful for details: https://github.com/pyenv/pyenv/issues/1375#issuecomment-589964703

## Improvements

    - must have
      * update lab guides for Python language
      * test project on Windows

    - nice to have
        - fix flake8 warning (newer version of flake8 and/or pycodestyle=2.4+)
        - remove log files in the end of the test (or create them in folder)
        - enable macOS testing on Travis CI
        - enable appveyor testing?

    - optional
        - change license to MIT or something like that
        - implement one more topic as an excersize
        - overall code cleaning
        - remove `src` folders, uplevel their contents

## Notes

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