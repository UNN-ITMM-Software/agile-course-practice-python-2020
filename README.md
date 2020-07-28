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
   - Мика Мартин, Роберт Мартин "Принципы, паттерны и методики гибкой разработки
     на языке C#" ([pdf][book-agile])
   - Мартин Фаулер, Кент Бек и др. "Рефакторинг: улучшение существующего кода"
     ([pdf][book-refactoring])

<!-- LINKS PERMANENT -->
[cc3]:              http://creativecommons.org/licenses/by-sa/3.0/
[travis]:           https://travis-ci.org/GodfatherThe/agile-course-practice-python
[travis-badge]:     https://api.travis-ci.org/GodfatherThe/agile-course-practice-python.svg?branch=master
[coveralls]:        https://coveralls.io/github/GodfatherThe/agile-course-practice-python
[coveralls-badge]:  https://coveralls.io/repos/GodfatherThe/agile-course-practice-python/badge.svg?branch=master&service=github
[labs]:             https://github.com/UNN-VMK-Software/agile-course-practice/tree/master/docs
[control-questions]: https://github.com/UNN-VMK-Software/agile-course-theory/blob/master/slides/control-questions.md
[cheatsheet]:       https://docs.google.com/document/d/1QhdJOnSw-Gn_-WM9RWLzmxZMrWTB4EbyTkaNBWMGA3Y/edit
[book-agile]:       http://www.books.ru/books/printsipy-patterny-i-metodiki-gibkoi-razrabotki-na-yazyke-c-fail-pdf-864714/?show=1
[book-refactoring]: http://www.books.ru/books/refaktoring-uluchshenie-sushchestvuyushchego-koda-fail-pdf-552092/?show=1

<!-- LINKS UPDATABLE -->
[exam-questions]:   https://docs.google.com/spreadsheet/ccc?key=0AsBBkrQIoSbjdDBDS2FTb3B3d3ZlUldJcl9HUmtEaUE&authkey=CKGP8vYB&authkey=CKGP8vYB#gid=0
[hall-of-fame]:     https://docs.google.com/spreadsheets/d/1JXyJBOlLZ8yvMGVVAJ6U3uiH10mMzcm-6n77SWg3p9Q/edit?authkey=CNXx0YMC&authkey=CNXx0YMC#gid=823569082

<!-- NOTES

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
