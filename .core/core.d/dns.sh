#!/bin/bash

# Author: Simone Gentili (gensimone)

cat <<EOF | sudo tee /etc/resolv.conf 1>/dev/null
# ██████╗ ███╗   ██╗███████╗
# ██╔══██╗████╗  ██║██╔════╝
# ██║  ██║██╔██╗ ██║███████╗
# ██║  ██║██║╚██╗██║╚════██║
# ██████╔╝██║ ╚████║███████║
# ╚═════╝ ╚═╝  ╚═══╝╚══════╝
#
# Using Cloudflare DNS servers

nameserver 1.1.1.1
nameserver 1.0.0.1
EOF

sudo chattr +i /etc/resolv.conf
