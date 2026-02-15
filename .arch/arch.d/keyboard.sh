#!/bin/sh

sudo mkdir -vp /etc/X11/xorg.conf.d
cat <<EOF | sudo tee /etc/X11/xorg.conf.d/00-keyboard.conf 1>/dev/null
Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "us"
        Option "XkbModel" "pc105+inet"
        Option "XkbOptions" "ctrl:nocaps"
EndSection
EOF

