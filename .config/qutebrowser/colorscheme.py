#  ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
# ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
# ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
# ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
# ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
#  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝


col = {
        'black': '#121212',
        'abs_black': '#000000',
        'white': '#C7C7C7',
        'green': '#12F512',
        'red': '#FF0000',
        'yellow': '#A8AB6F'
}

# Completion
c.colors.completion.category.bg = col['black']
c.colors.completion.category.fg = col['green']
c.colors.completion.category.border.bottom = col['black']
c.colors.completion.category.border.top = col['black']
c.colors.completion.even.bg = col['black']
c.colors.completion.odd.bg = col['black']
c.colors.completion.fg = col['white']
c.colors.completion.item.selected.bg = col['green']
c.colors.completion.item.selected.border.bottom = col['black']
c.colors.completion.item.selected.border.top = col['black']
c.colors.completion.item.selected.fg = col['abs_black']
c.colors.completion.match.fg = col['green']
c.colors.completion.scrollbar.bg = col['black']
c.colors.completion.scrollbar.fg = col['green']

# Downloads
c.colors.downloads.bar.bg = col['black']
c.colors.downloads.error.bg = col['red']
c.colors.downloads.error.fg = col['black']
c.colors.downloads.stop.bg = col['black']
c.colors.downloads.stop.fg = col['white']
c.colors.downloads.system.bg = 'none'

# Hints
c.colors.hints.bg = col['black']
c.colors.hints.fg = col['white']
c.colors.hints.match.fg = col['green']

# Keyhint
c.colors.keyhint.bg = col['black']
c.colors.keyhint.fg = col['white']
c.colors.keyhint.suffix.fg = col['green']

# Messages
c.colors.messages.error.bg = col['red']
c.colors.messages.error.border = col['red']
c.colors.messages.error.fg = col['abs_black']
c.colors.messages.info.bg = col['black']
c.colors.messages.info.border = col['black']
c.colors.messages.info.fg = col['white']
c.colors.messages.warning.bg = col['yellow']
c.colors.messages.warning.border = col['yellow']
c.colors.messages.warning.fg = col['abs_black']

# Prompt
c.colors.prompts.bg = col['black']
c.colors.prompts.border = col['black']
c.colors.prompts.fg = col['green']
c.colors.prompts.selected.bg = col['green']
c.colors.prompts.selected.fg = col['abs_black']


# # Statusbar
c.colors.statusbar.caret.bg = col['black']
c.colors.statusbar.caret.fg = col['white']
c.colors.statusbar.caret.selection.bg = col['green']
c.colors.statusbar.caret.selection.fg = col['abs_black']
c.colors.statusbar.command.bg = col['black']
c.colors.statusbar.command.fg = col['green']
c.colors.statusbar.insert.bg = col['black']
c.colors.statusbar.insert.fg = col['green']
c.colors.statusbar.normal.bg = col['black']
c.colors.statusbar.normal.fg = col['green']
c.colors.statusbar.passthrough.bg = col['black']
c.colors.statusbar.passthrough.fg = col['green']
c.colors.statusbar.private.bg = col['black']
c.colors.statusbar.private.fg = col['black']
c.colors.statusbar.command.private.bg = col['black']
c.colors.statusbar.command.private.fg = col['green']
c.colors.statusbar.progress.bg = col['green']
c.colors.statusbar.url.error.fg = col['red']
c.colors.statusbar.url.fg = col['green']
c.colors.statusbar.url.hover.fg = col['green']
c.colors.statusbar.url.success.http.fg = col['green']
c.colors.statusbar.url.success.https.fg = col['green']
c.colors.statusbar.url.warn.fg = col['yellow']

# Tabs
c.colors.tabs.indicator.system = 'none'
c.colors.tabs.bar.bg = col['black']
c.colors.tabs.even.bg = col['black']
c.colors.tabs.even.fg = col['white']
c.colors.tabs.indicator.error = col['red']
c.colors.tabs.indicator.start = col['white']
c.colors.tabs.indicator.stop = col['yellow']
c.colors.tabs.odd.bg = col['black']
c.colors.tabs.odd.fg = col['white']
c.colors.tabs.selected.even.bg = col['green']
c.colors.tabs.selected.even.fg = col['abs_black']
c.colors.tabs.selected.odd.bg = col['green']
c.colors.tabs.selected.odd.fg = col['abs_black']

# # Web Page
c.colors.webpage.bg = 'black'
