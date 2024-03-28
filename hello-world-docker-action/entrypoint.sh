#!/bin/sh -l

ls ./hello-world-docker-action -la
sudo apt install python3 -y
python3 test.py

echo "Hello $1"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT