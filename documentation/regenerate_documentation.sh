#! /usr/bin/env sh

sudo rm -rf build
sudo rm -rf source/_autosummary
make html
ln -sf build/html/index.html documentation.html
