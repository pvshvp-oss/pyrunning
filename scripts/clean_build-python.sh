#! /usr/bin/env sh

rm -rf build dist fenix_library*.egg-info
python -m build

mv build packaging/python/
mv dist packaging/python/
mv *.egg-info packaging/python/
