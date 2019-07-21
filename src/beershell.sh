#!/bin/bash

CONTAINER=$1
echo "Entering django shell in ${CONTAINER}"
podman exec -ti ${CONTAINER} /code/src/manage.py shell
