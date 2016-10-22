#!/usr/bin/env bash
# A script to test whether the Greenplum tests should be done or not
set -eu

cd "$(dirname "$0")"
. ./env.sh
{
    # check database version
    [[ "$(DBNAME=postgres timeout 1s db-execute "COPY (SELECT VERSION() LIKE '%Postgres-XL%') TO STDOUT")" == t ]]  # TODO move this check to db-init?
} &>/dev/null
