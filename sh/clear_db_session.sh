#!/bin/bash


echo "Start clearing..."
source /home/kachnic_1186205/Projects/.environments/DataDive/bin/activate
cd /home/kachnic_1186205/Projects/DataDive
# workon DataDive
python3 manage.py clearsessions
# deactivate
deactivate

echo "Cleared sessions"