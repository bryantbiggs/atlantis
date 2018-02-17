# Atlantis

A web application that loads records into a PostgreSQL database from an uploaded text file.

[![Build Status](https://travis-ci.com/bryantbiggs/atlantis.svg?token=wxLkaZqzrqBdTjth4HdJ&branch=master)](https://travis-ci.com/bryantbiggs/atlantis)
[![Maintainability](https://api.codeclimate.com/v1/badges/a668316c360493327748/maintainability)](https://codeclimate.com/repos/5a88578633cc3602a9000728/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a668316c360493327748/test_coverage)](https://codeclimate.com/repos/5a88578633cc3602a9000728/test_coverage)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- ##### virtualenv [optional]

The python package `virtualenv` is a tool to create isolated Python environments. If you do not have `virtualenv` installed, execute the following:

```bash
  $ pip install virtualenv
  $ virtualenv -p <path/to/local/python3.6.4+> <.nameofvirtualenv/>
```

It is not required to use `virtualenv` - `virtualenvwrapper` or other isolated environments are acceptable. The important note here is a working environment with Python 3.6.4+ and the modules listed in `requirements.txt` installed in that environment.

- ##### direnv [optional]

The application `direnv` enables us to inject variables into the application namespace via the bash native `export XXX=...`. Upon entering the directory containing a `.envrc` file via the command line, `direnv` will execute that file and load any variables and run any setup scripts provided in the config file. Upon leaving the directory (`cd ..`), it will also unset any exported environment variables to prevent leakage of environment variables into the operating systems current namespace.

`direnv` is not required, but the environment variables contained within the `.envrc.example` file are required to be set in your environment namespace prior to running the application. If wish to install `direnv`, see the [documentaton here](https://github.com/direnv/direnv) to get setup.

### Setup

Execute the following series of commands to populate the projects `virtualenv` (virtual environment)

First, create a copy of the `.envrc.example` file as `.envrc` and update the `.envrc` file with the appropriate values:

```bash
  $ cp .envrc.example .envrc && vim .envrc
  $ direnv allow
```

Note - Any new changes to the `.envrc` file will require the command `direnv allow` to be re-issued to permit the changes to take effect. The environment variables listed in the `.envrc.example` file are required for the project and should be populated with the appropriate values.

Finally, activate the virtual environment created above and install the required modules:

```bash
  $ source <.nameofvirtualenv>/bin/activate
  $ pip install -r requirements.txt
```

### Coding style tests

- ##### Python

To run the Python linter and check your code against [PEP8 compliance](https://www.python.org/dev/peps/pep-0008/):

```bash
  $ python3.6 -m flake8 <directory/>
```

Where <directory> is the directory you want to analyze. To check specific files replace `<directory>/` with the specific file you wish to analyze.

- ##### SQL

To run the SQL linter and check your code against ANSI SQL standard compliance:
```bash
  $ pip install pgsanity
  $ pgsanity <file.sql>
```

Where `<file.sql>` is the SQL script/file you want to analyze.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests.

## Changelog

Please see the [CHANGELOG.md](CHANGELOG.md) for details on individual releases.
