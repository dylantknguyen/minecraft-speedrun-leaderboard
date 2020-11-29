#!/bin/bash
PATH=$PATH:/usr/local/bin
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python3 main.py
