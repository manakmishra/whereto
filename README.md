# where<span></span>.to URL Shortener

where<span></span>.to is a simple URL Shortening tool, inspired from popular services like bit<span></span>.ly and tinyurl<span></span>.com.

Technologies Used:
- Python
- Django
- MongoDB
- Heroku for hosting (https://whereto-us.herokuapp.com/)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/manakmishra/whereto.git
$ cd whereto
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv) $ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv) $ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
