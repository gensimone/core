#!/bin/sh

check_dep() {
    if ! command -v $1 >/dev/null 2>&1; then
        printf "%s could not be found" $1 >&2
        exit 1
    fi
}

check_dep git
check_dep make
check_dep pkg-config

DWM="https://github.com/gensimone/dwm"
ST="https://github.com/gensimone/st"
DMENU="https://github.com/gensimone/dmenu"
