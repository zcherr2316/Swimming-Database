#!/bin/bash
export FLASK_APP=dbtour.py
nohup flask run -h 0.0.0.0 -p 10001 &
