#!/bin/bash

# Required to setup known database values in TravisCI
# Values set here are typically set through the AWS RDS console
psql -c "CREATE DATABASE ${DB_NAME};" -U postgres
psql -c "CREATE USER ${DB_USERNAME} WITH SUPERUSER LOGIN PASSWORD '${DB_PASSWORD}';" -U postgres
