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


## TODO
* Dockerfile
* CI




