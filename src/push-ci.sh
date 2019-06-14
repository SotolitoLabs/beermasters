#!/bin/bash

# Wrapper script for pushing to CI

echo "Pushing to upstream"
git push
echo "Pushing to CI"
git push ci-repo master
