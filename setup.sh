#!/bin/bash

# Create the virtual environment
python3.10 -m venv venv

# Install the dependencies
pip install -r requirements.txt

source venv/bin/activate