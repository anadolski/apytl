#!/usr/bin/env bash

echo Uninstalling package files
rm $(cat ./.installed_files.txt)
echo Done
