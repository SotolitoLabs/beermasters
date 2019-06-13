# Hacking 

## Environment
Development is done using a common docker image to avoid environment inconsistencies.
The Docker image is based on the latest stable CentOS and the django packages user are the ones included on the 
distro, exceptions are made when the python package is not included.

All code should include testing.

All code contributions should be pushed as a PR


### Running
```
docker run -ti -v `pwd`:/code --name test-django sotolito/django django-admin startproject /code
```


### Database setup

The application relies on a database that resides in a Podman container. The following steps describe the procedure to configure the database

Execute the script postgres_up.sh located in /src . This script will create the container from the latest postgres image

Once the container has been created, we have to login into it to finish configuring it

```

docker exec -it dev_postgres /bin/bash

su - postgres


CREATE DATABASE trydjango;

CREATE USER devuser WITH PASSWORD 'copacervecera';

ALTER ROLE devuser SET client_encoding TO 'utf8';
ALTER ROLE devuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE devuser SET timezone TO 'UTC';


GRANT ALL PRIVILEGES ON DATABASE trydjango TO devuser;

\q

exit  // from postgres user

exit  // from container
```


## TODO
* Dockerfile
* CI




