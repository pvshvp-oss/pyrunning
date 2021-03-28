#! /usr/bin/env sh

python -m build

mv build packaging/python/
mv dist packaging/python/
mv *.egg-info packaging/python/
