#!/bin/bash

python ping.py &
python measures.py &
python push.py &

