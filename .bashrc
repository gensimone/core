#
# ~/.bashrc #

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

append_path() {
	case ":$PATH:" in
	*:"$1":*) ;;
	*)
		PATH="$1:${PATH:+$PATH}"
		;;
	esac
}

append_path $HOME/.cargo/bin
append_path $HOME/.local/bin

# PS1='[\W]$ '
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

set -o ignoreeof # Same as setting IGNOREEOF=10
set -o vi

export PAGER=less
export VISUAL=vi
export EDITOR=nvim
export PROMPT_COMMAND="echo"
export PYTHON_BASIC_REPL=1

if [ -f ~/.bash_aliases ]; then
	. ~/.bash_aliases
fi

eval "$(fzf --bash)"
