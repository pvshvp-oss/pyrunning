#! /usr/bin/env sh

# Clean pipenv
pipenv uninstall fenix-library-running fenix-library-configuration sphinx sphinx-rtd-theme sphinxcontrib-mermaid setuptools build
sudo pipenv uninstall fenix-library-running fenix-library-configuration sphinx sphinx-rtd-theme sphinxcontrib-mermaid setuptools build
pipenv clean
sudo pipenv clean
pipenv --rm
sudo pipenv --rm

# Check if pipenv is cleaned
pipenv graph
sudo pipenv graph

# Regenerate pipenv
sudo pipenv install --dev -e git+https://gitlab.com/rebornos-team/fenix/libraries/running.git#egg=fenix_library-running -e git+https://gitlab.com/rebornos-team/fenix/libraries/configuration.git#egg=fenix_library-configuration sphinx sphinx-rtd-theme sphinxcontrib-mermaid setuptools build

# Check if pipenv is regenerated
pipenv graph
sudo pipenv graph