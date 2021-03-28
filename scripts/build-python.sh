#! /usr/bin/env sh

rm -rf build dist fenix_library*.egg-info
rm -rf packaging/python/build packaging/python/dist packaging/python/fenix_library*.egg-info
python -m build

mv -f build packaging/python/
mv -f dist packaging/python/
mv -f *.egg-info packaging/python/
