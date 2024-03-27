#!/bin/sh -l

ls -la

echo "Hello $1"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT