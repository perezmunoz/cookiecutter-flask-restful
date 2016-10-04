cookiecutter-flask-restful
==========================

Cookiecutter template for the Flask-RESTful API. Based on the [Iris dataset](http://archive.ics.uci.edu/ml/datasets/Iris), this API returns 5 random Iris samples from the database. Currently there is only one endpoint `GET /api/v1/iris` handled.

Use it now
----------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/perezmunoz/cookiecutter-flask-restful.git

Basic info will be asked (name, project name, app name, etc.) and setup in your newly created repository.

Install dependencies using [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io)

    $ mkvirtualenv cookiecutter-flask-restful
    $ pip install -r requirements.txt

To launch the app, run the following

    $ python api.py

Request for Iris data at the command line

    $ curl -i -X GET http://127.0.0.1:5000/api/v1/iris