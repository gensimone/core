#!/bin/sh

install() {
    name="$(basename $1)"
    git clone --depth=1 $1 $name && sudo make clean install -C $name && rm -rfv $name
    [ $? -gt 0 ] && echo "Aborted." >&2 && exit 1
}

install "https://github.com/gensimone/dwm"
install "https://github.com/gensimone/st"
install "https://github.com/gensimone/dmenu"

sudo mkdir -vp /usr/share/xsessions
cat <<EOF | sudo tee /usr/share/xsessions/dwm.desktop 1>/dev/null
[Desktop Entry]
Name=dwm
Exec=dwm
Type=XSession
Icon=dwm
EOF
