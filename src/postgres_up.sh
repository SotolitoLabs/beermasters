#!/bin/bash

podman run --name bm_postgres --network="host" -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=anygivenpassword -d postgres
