#!/bin/sh

DWM="https://github.com/gensimone/dwm"
ST="https://github.com/gensimone/st"
DMENU="https://github.com/gensimone/dmenu"
SLSTATUS="https://github.com/gensimone/slstatus"

install() {
    git clone --depth=1 $1 $2 && sudo make clean install -C $2 && rm -rfv $2
    [ $? -gt 0 ] && echo "Aborted." >&2 && exit 1
}

#       repo      pkg name
install $DWM      dwm
install $ST       st
install $DMENU    dmenu
install $SLSTATUS slstatus

sudo mkdir -vp /usr/share/xsessions
cat <<EOF | sudo tee /usr/share/xsessions/dwm.desktop 1>/dev/null
[Desktop Entry]
Name=dwm
Exec=dwm
Type=XSession
Icon=dwm
EOF
