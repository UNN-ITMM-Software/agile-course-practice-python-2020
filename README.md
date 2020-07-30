# Спецкурс Agile Development, Python Edition

[![Join the chat][gitter-badge]][gitter-chat]
[![Build Status][travis-badge]][travis]
[![Coverage Status][coveralls-badge]][coveralls]
[![License: CC BY-SA 4.0][license-badge]][license]

 - Нижегородский Государственный Университет им. Н.И. Лобачевского
 - Институт ИТММ, каф. МОСТ

## Ресурсы

- [Таблица успеваемости][hall-of-fame]
- Учебные материалы
    - [Описания лабораторных работ][lab-guide]
    - [Контрольные вопросы][quiz], [колхозная шпаргалка][cheatsheet] к ним
    - [Экзаменационные вопросы][exam-questions]
- Литература
    - Мика Мартин, Роберт Мартин "Принципы, паттерны и методики гибкой разработки на языке C#" ([pdf][book-agile])
    - Мартин Фаулер, Кент Бек и др. "Рефакторинг: улучшение существующего кода" ([pdf][book-refactoring])

<!-- LINKS UPDATABLE -->
[hall-of-fame]:     https://docs.google.com/spreadsheets/d/1Pt9i-UGUiFG8_tjnUjxmCqVjP9VHG9GJc1LNZQeGU_4/edit#gid=1613595355

<!-- LINKS PERMANENT -->
[license]:          http://creativecommons.org/licenses/by-sa/4.0/
[license-badge]:    https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[travis]:           https://travis-ci.org/UNN-ITMM-Software/agile-course-practice-python
[travis-badge]:     https://travis-ci.org/UNN-ITMM-Software/agile-course-practice-python.svg?branch=master
[coveralls]:        https://coveralls.io/github/UNN-ITMM-Software/agile-course-practice-python?branch=master
[coveralls-badge]:  https://coveralls.io/repos/github/UNN-ITMM-Software/agile-course-practice-python/badge.svg?branch=master
[gitter-chat]:      https://gitter.im/agile-course-practice-python/community
[gitter-badge]:     https://badges.gitter.im/Lobby.svg

[book-agile]:       http://www.books.ru/books/printsipy-patterny-i-metodiki-gibkoi-razrabotki-na-yazyke-c-fail-pdf-864714/?show=1
[book-refactoring]: http://www.books.ru/books/refaktoring-uluchshenie-sushchestvuyushchego-koda-fail-pdf-552092/?show=1

[lab-guide]:        https://github.com/UNN-VMK-Software/agile-course-practice-python/tree/master/docs
[quiz]:             https://github.com/UNN-VMK-Software/agile-course-theory/blob/master/slides/control-questions.md
[cheatsheet]:       https://docs.google.com/document/d/1QhdJOnSw-Gn_-WM9RWLzmxZMrWTB4EbyTkaNBWMGA3Y/edit
[exam-questions]:   https://docs.google.com/spreadsheets/d/1Pt9i-UGUiFG8_tjnUjxmCqVjP9VHG9GJc1LNZQeGU_4/edit#gid=827430395

<!-- NOTES

TODO

    - code
        - migrate to newer version of Python
        - remove log files in the end of the test
        - overall code cleaning
        - implement one more topic as an excersize
    - infrastructure
        - update lab guides for Python
        - whether and how to use Python virtualenv
        - change license to MIT or something like that
        - also enable macOS testing on Travis CI

NOTES

    - on macOS used default Python2.7
    - without pip installed nose using $sudo easy_install nose, all tests have passed

   69  easy_install pip
   70  sudo easy_install pip
   95  pip install -r requirements.txt

   80  python -m pip install flake8
   87  pip install zipp==0.5.0
   88  pip install contextlib2 pathlib2
   89  pip install configparser==3.5
   99  PATH="/Users/kirill-personal/Library/Python/2.7/bin:$PATH"

-->
