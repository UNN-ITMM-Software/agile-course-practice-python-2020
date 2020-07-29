# Спецкурс "Agile Development". Python версия репозитория

[![Build Status][travis-badge]][travis]
[![Coverage Status][coveralls-badge]][coveralls]

 - Нижегородский Государственный Университет им. Н.И. Лобачевского
 - Институт ИТММ, каф. МОСТ
 - __License__: Creative Commons Attribution-Share Alike 3.0 ([CC BY-SA 3.0][cc3])

## Ресурсы

- [Таблица успеваемости][hall-of-fame]
- Учебные материалы
    - [Описания лабораторных работ][labs]
    - [Контрольные вопросы][control-questions], [колхозная шпаргалка][cheatsheet] к ним
    - [Экзаменационные вопросы][exam-questions]
- Литература
    - Мика Мартин, Роберт Мартин "Принципы, паттерны и методики гибкой разработки на языке C#" ([pdf][book-agile])
    - Мартин Фаулер, Кент Бек и др. "Рефакторинг: улучшение существующего кода" ([pdf][book-refactoring])

<!-- LINKS UPDATABLE -->
[hall-of-fame]:     https://docs.google.com/spreadsheets/d/1Pt9i-UGUiFG8_tjnUjxmCqVjP9VHG9GJc1LNZQeGU_4/edit#gid=1613595355
[exam-questions]:   https://docs.google.com/spreadsheets/d/1Pt9i-UGUiFG8_tjnUjxmCqVjP9VHG9GJc1LNZQeGU_4/edit#gid=827430395

<!-- LINKS PERMANENT -->
[cc3]:              http://creativecommons.org/licenses/by-sa/3.0/
[travis]:           https://travis-ci.org/UNN-ITMM-Software/agile-course-practice-python
[travis-badge]:     https://travis-ci.org/UNN-ITMM-Software/agile-course-practice-python.svg?branch=master
[control-questions]: https://github.com/UNN-VMK-Software/agile-course-theory/blob/master/slides/control-questions.md
[cheatsheet]:       https://docs.google.com/document/d/1QhdJOnSw-Gn_-WM9RWLzmxZMrWTB4EbyTkaNBWMGA3Y/edit
[book-agile]:       http://www.books.ru/books/printsipy-patterny-i-metodiki-gibkoi-razrabotki-na-yazyke-c-fail-pdf-864714/?show=1
[book-refactoring]: http://www.books.ru/books/refaktoring-uluchshenie-sushchestvuyushchego-koda-fail-pdf-552092/?show=1

<!-- CLEANUP -->
[coveralls]:        https://coveralls.io/github/GodfatherThe/agile-course-practice-python
[coveralls-badge]:  https://coveralls.io/repos/GodfatherThe/agile-course-practice-python/badge.svg?branch=master&service=github
[labs]:             https://github.com/UNN-VMK-Software/agile-course-practice/tree/master/docs

<!-- NOTES

TODO

    - infrastructure
        - refresh links
        - enable GitterChat
        - update lab guides for Python
    - code
        - resolve issue with flake8 (first locally, then remotely)
        - make code coverage report the same both locally and on Travis-CI
        - enable code coverage

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

  101  flake8 --max-line-length=110 code

-->
