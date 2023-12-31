#! /usr/bin/env sh

SCRIPT_DIRECTORY="$(dirname -- "$(readlink -f -- "$0")")"
PROJECT_DIRECTORY="$(dirname -- "$SCRIPT_DIRECTORY")"

(   cd "$PROJECT_DIRECTORY/documentation" \
    && make html \
    && ln -sf build/html/index.html documentation.html
)
