#!/bin/bash

# Setup database with read and write users groups and roles
export PGPASSWORD=$DB_PASSWORD

psql -h $DB_HOST -p 5432 -U $DB_USERNAME $DB_NAME -c \
"""CREATE ROLE grp_crud WITH NOINHERIT NOLOGIN;
COMMENT ON ROLE grp_crud IS 'Group - Create Read Update Delete';
CREATE ROLE crud_user WITH INHERIT LOGIN PASSWORD '${CRUD_USER_PASSWORD}' IN ROLE grp_crud;
COMMENT ON ROLE crud_user IS 'User - Create Read Update Delete';
CREATE ROLE grp_read WITH NOINHERIT NOLOGIN;
COMMENT ON ROLE grp_read IS 'Group - Read';
CREATE ROLE read_user WITH INHERIT LOGIN PASSWORD '${READ_USER_PASSWORD}' IN ROLE grp_read;
COMMENT ON ROLE read_user IS 'User - Read';
GRANT grp_crud TO superadmin;
GRANT grp_read TO superadmin;"""
