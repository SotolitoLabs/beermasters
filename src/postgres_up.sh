#!/bin/bash

podman run --name bm_postgres -e POSTGRES_PASSWORD=beerM@ster01 -d postgres
