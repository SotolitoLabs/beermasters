#!/bin/bash

echo "Entering django shell in $1"
podman exec -ti $1 /code/manage.py shell
