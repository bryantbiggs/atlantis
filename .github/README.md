# Atlantis

A web application that loads records into a PostgreSQL database from an uploaded text file.

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![Build Status](https://travis-ci.org/bryantbiggs/atlantis.svg?branch=develop)](https://travis-ci.org/bryantbiggs/atlantis)
[![Maintainability](https://api.codeclimate.com/v1/badges/8eba154e2597628d0234/maintainability)](https://codeclimate.com/github/bryantbiggs/atlantis/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8eba154e2597628d0234/test_coverage)](https://codeclimate.com/github/bryantbiggs/atlantis/test_coverage)
[![Greenkeeper badge](https://badges.greenkeeper.io/bryantbiggs/atlantis.svg)](https://greenkeeper.io/)

## Getting Started

The following instructions will help you setup your own project for development and testing purposes.

### Prerequisites

- #### AWS

This project is deployed and developed with tools that rely on Amazon Web Services. You can use the [`aws-cli`](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html) interface to provision the credentials file or by performing the following steps;

1. Create an `aws` directory with `credentials` and `config` files:

```bash
    $ mkdir ~/.aws
    $ touch ~/.aws/credentials
    $ touch ~/.aws/config
```

2. Copy the following definition into the `credentials` file, filling in your specific values:

```
[profile atlantis]
aws_access_key_id=<YOUR-AWS-ACESS-KEY-ID>
aws_secret_access_key=<YOUR-AWS-SECRET-ACCESS-KEY>
```

Copy the following definition into the `config` file (change `region` to suite):

```
[profile atlantis]
region=us-east-1
```

- #### NPM

The `serverless` framework is a Nodejs application and requires `npm` (>=5.x).

Install the projects `serverless` dependencies locally by running the following command.

```bash
    $ npm i
```

### Setup

1. Register a web domain through AWS Route53 or another domain provider

2. Create an AWS S3 bucket with the same name as your registered domain - i.e. `mycoolwebsite.com` - and provision the bucket to host a static website (see more instructions [here](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/static-website-hosting.html) for setting up S3 buckets for website hosting)

3. Copy the `env.yml.example` file to `env.yml` and populate the associated values for your project:

```bash
    $ cp env.yml.example env.yml && vim env.yml
```

4. Create a Route53 record for API endpoint url using the `serverless-domain-manager` package:

```bash
    $ sls create_domain --aws-profile atlantis
```

5. Upload static content to S3 bucket for website content using the `serverless-finch` package:

```bash
    $ sls client deploy --aws-profile atlantis
```

### Deployment

To provision the necessary AWS resources and deploy the project:

```base
    $ sls deploy --aws-deploy atlantis
```

### Coding style tests

- #### Python

To run the Python linter and check your code against [PEP8 compliance](https://www.python.org/dev/peps/pep-0008/):

```bash
    $ pip install flake8
    $ python3.6 -m flake8 <directory/>
```

Where <directory> is the directory you want to analyze. To check specific files replace `<directory>/` with the specific file you wish to analyze.

- #### SQL

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
