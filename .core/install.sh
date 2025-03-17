#!/bin/bash

#  ██████╗ ██████╗ ██████╗ ███████╗
# ██╔════╝██╔═══██╗██╔══██╗██╔════╝
# ██║     ██║   ██║██████╔╝█████╗
# ██║     ██║   ██║██╔══██╗██╔══╝
# ╚██████╗╚██████╔╝██║  ██║███████╗
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Author: Simone Gentili (gensimone)

here="$(cd "$(dirname "$0")" || exit 1; pwd -P)"

# Utility function that iterates over the lines of
# the file at path $1 and invokes the $2 function
# on each of the lines that do not start with the
# '#' symbol.
exec_func() {
  while IFS= read -r line; do
    if ! [[ "$line" =~ ^[[:space:]]*# ]]; then
      "$2" "$line"
    fi
  done < "$here/$1"
}

# Create $HOME/ dirs
create_dirs() {
  mkdir -pv "$HOME/$1"
}

exec_func "$here/dirs" create_dirs

if cd "$here"/core.d; then
  for file in *.sh; do
    ./"$file"
  done
fi
