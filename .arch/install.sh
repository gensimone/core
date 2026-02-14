#!/bin/sh

ROOT="$(cd "$(dirname "$0")" || exit 1; pwd -P)"

if ! sudo pacman --needed --noconfirm -Syu -< ./pkgs; then
    exit 1
    echo "Aborted" >&2
fi

exec_func() {
  while IFS= read -r line; do
    if ! [[ "$line" =~ ^[[:space:]]*# ]] && [ -n "$line" ]; then
      "$2" "$line"
    fi
  done < "$1"
}

enable_user_service() {
    systemctl --user enable $1
}

enable_system_wide_service() {
    sudo systemctl enable $1
}

add_user_to_group() {
  sudo usermod -aG "$1" "$USER"
}

exec_func "$ROOT/user-services"        enable_user_service
exec_func "$ROOT/system-wide-services" enable_system_wide_service
exec_func "$ROOT/groups"               add_user_to_group

for file in $ROOT/arch.d/*.sh; do
    ./"$file"
done
