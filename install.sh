#!/usr/bin/env bash

echo Building package
python setup.py build
echo ''
echo Installing package
python setup.py install --user
