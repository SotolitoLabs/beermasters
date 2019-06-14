#!/bin/bash

# Wrapper script for pushing to CI
# Beermasters

echo "Pushing Beermasters to upstream"
git push
echo "Pushing to CI"
git push ci-repo master
