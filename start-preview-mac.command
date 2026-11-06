#!/bin/bash
cd "$(dirname "$0")"
( sleep 1.5; open "http://localhost:8080" ) &
python3 _preview_server.py
