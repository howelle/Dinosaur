# lemur
Notes about the Bio data collector
# Development Notes
Some notes on the necessary vocabulary and material needed to understand app development.
Try `command + f` to search for a word

## Contents:
* Pip (Python Package Index)
	Pip is a package manager for Python packages. Using `pip install ___` in terminal will help to obtain the __ package
* Text editors
	* Markdown
	* Sublime
		* Sublime Package Control: if using sublime make sure to download the package manager, which will allow you to install packages and add ons. The command for opening the text console (where package control is installed) is `control + backtick` and the command for opening package control is `command + shift + p`
	* Latex
	* EMACs
* Coding Style
	* Linters
	* PEP8
	* Python Sphinx (documentation generator)
* IDE
* Homebrew
	Homebrew is a Package Manager that helps with installing a lot of the necessary software for development
* Version Control
* Virtual Environment & Virtualenvwrapper
	*Git/Github

* W3C - (https://www.w3.org/)
* AJAX/AJAJ
	* JSON
* Web Server
	* Apache
	* Nginx
* WSGI
	* Gunicorn
* Network Protocols
	How computers communicate/format and protocol for communication
	* SSH (Secure Shell)
	* FTP (File Transfer Protocol)
	* *TCP* (Transmission Control Protocol)
	* *HTTP* (Hyper Text Transfer Protocol)
* Cloud Computing
	* SaaS 
	* PaaS
		* Heroku
	* IaaS
* Operating System
	* Linux
	* Ubuntu
* Framework
	* Flask
	* Django
	* Bottle
* Database
	* ORM (Object Relational Mapper)
		* SQLAlchemy
		* Django ORM
	* Database Connector
		* psycopg
	* Relational Databases
		* SQL - Relational Database Management System 
			* PostgreSQL 
		* MongoDB
	* queries, cte, regular expressions
	* BONUS: CAM (Content Addressable Memory)
* Formats
	* HTML (Hypertext markup language)
	* CSS
	* Javascript
	* JQuery
	* Bootstrap
* Template Engine
	* Jinga2
* Interface
	* GUI
	* API
* Other Dependencies
	* WTForms
	* Celery

* Security
	* SHA-1 hash
	* SQL Injection Attack

* Other Languages
	* Python
	* Ruby
	* Lisp
	* Basic
	* Haskell
	* Scala
	* C, C++
	* Java

## Part 1 Getting Started: 
### Git Command Help
* Instructions: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html
* CheatSheet: https://education.github.com/git-cheat-sheet-education.pdf
* More: https://github.com/reed-college/2016_sds_lesson_notes/blob/master/lesson_02_git.markdown

### Markdown
* Guide: https://en.support.wordpress.com/markdown-quick-reference/
* Guide with table info: https://guides.github.com/features/mastering-markdown/

### Virtual Environment
* Setting it up: https://github.com/reed-college/2016_sds_lesson_notes/blob/master/lesson_03_beginning_development.markdown

### Install/Download:
SO MANY THINGS! HERE ARE A FEW:
* SublimeLinter: http://www.sublimelinter.com/en/latest/
	* Flake8: https://github.com/SublimeLinter/SublimeLinter-flake8

###S Create requirements.txt File With All Dependencies Listed
Our application must have a requirements.txt that contains all the package dependencies with the exact versions.
```pip freeze > requirements.txt```

### Database
We’ll need to get a Postgres database set up to store our todo list. We’ll also add Python ORM SQLAlchemy to our app. Once you have Postgres installed, create a database and name it lemur to use as a local database.<br\>
* Run PostgreSQL command line client.<br\>
* Create a database user with a password.<br\>
* Create a database instance.<br\>

## Part2 Moving Forward:
### Application Organization and Tutorials
* Tutorial for Whole Process: http://www.vertabelo.com/blog/technical-articles/web-app-development-with-flask-sqlalchemy-bootstrap-part-1
* Tutorial: http://blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
* Tutorial: https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

## Part3 Particular Components:
### HTML
* Mozilla Guide (start here!): https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction
	* https://developer.mozilla.org/en-US/docs/Web/HTML
	* https://developer.mozilla.org/en-US/docs/Web/HTML/Element
	* https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input

#### CSS

### Bootstrap
* Download: http://getbootstrap.com/getting-started/#download
* Nav-bar: http://getbootstrap.com/components/#navbar
* Nav-bar: http://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-navbar.php
* Components: http://getbootstrap.com/css/

### Flask 
* Potential Flask App Structure: http://gouthamanbalaraman.com/blog/flask-app-directory-structure.html
* Flask Resources: https://www.fullstackpython.com/flask.html


### Jinja Templates:
* http://jinja.pocoo.org/docs/dev/templates/

### WTForms:
* http://wtforms.readthedocs.io/en/latest/crash_course.html

### PostgreSQL:
* Creating Database etc.: http://www.postgresql.org/docs/8.0/static/tutorial-createdb.html

### jQuery:
* Tutorial: http://www.tutorialrepublic.com/jquery-tutorial/jquery-syntax.php
* Tutorial: https://www.codecademy.com/courses/web-beginner-en-bay3D/2/3?curriculum_id=50a3fad8c7a770b5fd0007a1

## Extra Stuff:
* Javascript thing: https://d3js.org/
* Python Style Guide: https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds
*orgmode