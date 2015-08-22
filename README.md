# listenlocally app

This app exists to:
* Provide geographically contextualized music recommendations (various sources)
* Quickly provide 30-sec samples of music by artists playing locally
* 

This is a basic Python/Django app, based on the [Heroku Tutorial][Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ sudo apt-get install libpq-dev (required on Ubuntu 14.04)
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

## Documentation

TODO
