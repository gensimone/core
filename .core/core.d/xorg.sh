#!/bin/bash

# ██╗  ██╗ ██████╗ ██████╗  ██████╗
# ╚██╗██╔╝██╔═══██╗██╔══██╗██╔════╝
#  ╚███╔╝ ██║   ██║██████╔╝██║  ███╗
#  ██╔██╗ ██║   ██║██╔══██╗██║   ██║
# ██╔╝ ██╗╚██████╔╝██║  ██║╚██████╔╝
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝

# Author: Simone Gentili (gensimone)

sudo mkdir -p /etc/X11/xorg.conf.d

# Keyboard: caps lock as ctrl
cat <<EOF | sudo tee /etc/X11/xorg.conf.d/00-keyboard.conf 1>/dev/null
Section "InputClass"
    Identifier "system-keyboard"
    MatchIsKeyboard "on"
    Option "XkbOptions" "ctrl:nocaps"
EndSection
EOF

# Touchpad: enables tapping
cat <<EOF | sudo tee /etc/X11/xorg.conf.d/40-libinput.conf 1>/dev/null
Section "InputClass"
    Identifier "libinput touchpad catchall"
    MatchIsTouchpad "on"
    MatchDevicePath "/dev/input/event*"
    Driver "libinput"
    Option "Tapping" "on"
EndSection
EOF
