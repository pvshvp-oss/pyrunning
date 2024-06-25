#! /bin/bash

script_dir=$(dirname "$(realpath "$0")")
echo "script_dir: $script_dir"
cd "$script_dir/../../.."
ln -sv "$script_dir/debian" debian
EDITOR=nano gbp dch --debian-branch=main --release --dch-opt=--upstream -a
unlink debian