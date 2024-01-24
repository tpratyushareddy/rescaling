#!/bin/bash

set -ex

# Source env.sh to read all the vars
source /root/main_env.sh
source /root/env.sh

ls -la /root/.kube

source /root/common_run.sh
checks
config_setup

# Substitute config with environment vars defined
envsubst < D:\OneDrive\Desktop\rescaling\rescaling\application_outages\app_outages.yaml.templete > /root/kraken/scenarios/app_outage.yaml
envsubst < D:\OneDrive\Desktop\rescaling\rescaling\config.yml > /root/kraken/config/app_outage_config.yaml

# Run Kraken
cd /root/kraken


python3.9 run_kraken.py --config=config/app_outage_config.yaml