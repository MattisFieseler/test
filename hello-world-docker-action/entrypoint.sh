#!/bin/sh -l

ls ./hello-world-docker-action -la
python3

echo "Hello $1"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT