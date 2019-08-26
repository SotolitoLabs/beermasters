#!/bin/bash

PASS="anygivenpassword"

if [[ "${1}" != "" ]]; then
    PASS=$1
fi

podman run --name bm_postgres --network="host" -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=${PASS} -d postgres
