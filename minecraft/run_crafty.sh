#!/bin/bash
cd /workspaces/minecraft-server-24-7/minecraft
source .venv/bin/activate 
cd crafty-4 
exec python3 main.py 
