#!/bin/sh

DWM="https://github.com/gensimone/dwm"
ST="https://github.com/gensimone/st"
DMENU="https://github.com/gensimone/dmenu"
SLSTATUS="https://github.com/gensimone/slstatus"

install() {
    if ! git clone $1 $2 && make -C $2 && rm -rfv $2; then
        echo "Aborted." >&2
        exit 1
    fi
}

#       repo     pkg name
install dwm      dwm
install st       st
install dmenu    dmenu
install slstatus slstatus
