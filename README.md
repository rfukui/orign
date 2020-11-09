# Test ORIGN v.0.0.1

**This code is a part of ORIGN coding test**

**All code was written in PYTHON**

## Requirements to run and test the API:

Install [docker-compose](https://docs.docker.com/compose/install/)

```sh
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```
Test the installation of docker-compose
```sh
$ docker-compose --version
```

## Running the app in development mode:

Execute:
```
$ docker-compose up dev
```

Once installed, the API will run on the 5000 port at localhost:
`http://localhost:5000/`

## Architecture

The application was constructed with separation between controllers and services, to provide an easy way of creating new validations, calculations and risks.

## Tests

To run the tests, execute the following command:

```sh
$ docker-compose up test
```

## Roadmap

For the next steps I will use [Flask-RESTplus](https://flask-restplus.readthedocs.io/en/stable/) and create models.

With the use of RESTplus I will be able to do a better documentation with [swagger](https://flask-restplus.readthedocs.io/en/stable/swagger.html) and use models to improve data validation.
