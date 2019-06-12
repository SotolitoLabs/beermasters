#!/bin/bash

podman run --name bm_postgres -e POSTGRES_PASSWORD=b&&rMaster01 -d docker.io/postgres