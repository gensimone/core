# ██████╗  █████╗ ███████╗██╗  ██╗
# ██╔══██╗██╔══██╗██╔════╝██║  ██║
# ██████╔╝███████║███████╗███████║
# ██╔══██╗██╔══██║╚════██║██╔══██║
# ██████╔╝██║  ██║███████║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias rm='rm -i'
alias ln='ln -i'
alias cp='cp -i'
alias mv='mv -i'
alias df='df -h'
alias du='du -h'
alias so='syncorg'
alias v='nvim'
alias vi='nvim'
alias vim='nvim'
alias gpt='tgpt -m'
alias installed-on="sudo tune2fs -l /dev/nvme0n1p3 | grep created | awk '{print \$3,\$4,\$5,\$6,\$7}'"

# Enable starship
eval "$(starship init bash)"

set -o vi

[ -f "$HOME/.distro/.sbashrc" ] && . "$HOME/.distro/.sbashrc"
