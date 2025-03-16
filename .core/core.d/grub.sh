#!/bin/bash
#
# Author: Simone Gentili

cat <<EOF | sudo tee /etc/default/grub 1>/dev/null
#  ██████╗ ██████╗ ██╗   ██╗██████╗
# ██╔════╝ ██╔══██╗██║   ██║██╔══██╗
# ██║  ███╗██████╔╝██║   ██║██████╔╝
# ██║   ██║██╔══██╗██║   ██║██╔══██╗
# ╚██████╔╝██║  ██║╚██████╔╝██████╔╝
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

GRUB_DEFAULT=0
GRUB_TIMEOUT=1
GRUB_DISTRIBUTOR="Void"
GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3"
EOF

sudo update-grub
