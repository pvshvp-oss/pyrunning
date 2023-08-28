#! /usr/bin/env sh

SCRIPT_DIRECTORY="$(dirname -- "$(readlink -f -- "$0")")"
PROJECT_DIRECTORY="$(dirname -- "$SCRIPT_DIRECTORY")"

(   cd "$PROJECT_DIRECTORY"
    rm -rf build dist *.egg-info
    rm -rf packaging/python/build packaging/python/dist packaging/python/*.egg-info
    python -m build

    mv -f build packaging/python/
    mv -f dist packaging/python/
    mv -f *.egg-info packaging/python/
)