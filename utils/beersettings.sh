#!/bin/bash

# Poor man's deployer
# updates the git repo
# sets the db configuration

REPO="/home/repo"
SETTINGS="settings.py"
DBNAME="dbname"
USERNAME="username"
PW="password"

echo "Updating code"
cd $REPO
git pull

echo "Updating ${SETTINGS}"
sed -i s/DBNAME/${DBNAME}/ ${SETTINGS}
sed -i s/USERNAME/${USERNAME}/ ${SETTINGS}
sed -i s/PW/${PW}/ ${SETTINGS}

echo "be happy..."
