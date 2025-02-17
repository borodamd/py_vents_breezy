#!/bin/bash
#

alias python=python3

python3 setup.py build; 
python3 setup.py sdist;
sudo python3 setup.py install
