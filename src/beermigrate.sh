#!/bin/bash

CONTAINER=$1
echo "Running migrations in ${CONTAINER}"
podman exec -ti ${CONTAINER} /code/src/manage.py migrate
