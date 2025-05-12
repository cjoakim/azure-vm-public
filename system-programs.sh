#!/bin/bash

# Display the location and version of system programs.
# Chris Joakim, May 2025 

echo "git:"
which git
git --version

echo "python3:"
which python3
python3 --version

echo "pip:"
which pip
pip --version


# git:
# /usr/bin/git
# git version 2.43.0
# python3:
# /usr/bin/python3
# Python 3.12.3
# pip:
# /usr/bin/pip
# pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
