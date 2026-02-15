#!/bin/sh

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
