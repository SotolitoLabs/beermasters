#!/bin/bash

CONTAINER="test-django"

if [[ ${1} != "" ]]; then
    CONTAINER="$1"
fi

podman run --network="host" -p 127.0.0.1:8000:8000 --rm -ti -v `pwd`:/code --name $CONTAINER sotolito/django /code/src/manage.py runserver 0:8000
