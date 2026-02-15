#!/bin/sh

check_dep() {
    if ! command -v $1 >/dev/null 2>&1; then
        printf "%s could not be found\n" $1 >&2
        exit 1
    fi
}

check_dep gcc
check_dep git
check_dep libxft
check_dep libxinerama
check_dep make
check_dep pkg-config

DWM="https://github.com/gensimone/dwm"
ST="https://github.com/gensimone/st"
DMENU="https://github.com/gensimone/dmenu"

install() {
    if ! git clone $1 $2 && make -C $2 && rm -rfv $2; then
        echo "Aborted." >&2
        exit 1
    fi
}

install dwm
install st
install dmenu
