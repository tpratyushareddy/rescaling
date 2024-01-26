#!/bin/bash

# 'x' means verbose/debug output and 'e' is used for telling bash do not execute other lines of the code if there are any executing errors. Exit running the code.
set -ex

# Contains default values for congif.yml file if the data is not given by the user. 
source /app/containers/env.sh

# Substitute config with environment vars defined
envsubst < /app/containers/config.yml.template > /tmp/config.yml                                                       

# Run Rescaling 
cd /app                                     

python rescaling.py --config=/tmp/config.yml