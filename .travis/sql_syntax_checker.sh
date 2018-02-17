#!/bin/bash

# SQL sytnax evaluation
# Ensure that the SQL syntax utilized in *.sql files adhere to PostgreSQL standards

for FILE_NAME in $( find . -name '*.sql' ); do
    ERROR_LINES=$(pgsanity $FILE_NAME | wc -l)
    if [ "$ERROR_LINES" -gt "0" ]
    then
        pgsanity $FILE_NAME
        echo >&2 "[FAILED] The following file $FILE_NAME did not pass SQL syntax checker"
        exit 1
    fi
done

echo "[PASS] All *.sql files passed SQL syntax checker"
exit 0
