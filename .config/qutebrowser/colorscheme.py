matrix = {
    # matrix night
    'matrix0': '#0D0208',
    'matrix1': '#0D0208',
    'matrix2': '#0D0208',
    'matrix3': '#226622',
    # term
    'matrix4': '#c6c6c6',
    'matrix5': '#00ff41',
    'matrix6': '#c6c6c6',
    # green
    'matrix7': '#339933',
    'matrix8': '#0D0208',
    'matrix9': '#008F11',
    'matrix10': '#027c14',
    # errors-warnings
    'matrix11': '#ff0000',
    'matrix12': '#D08770',
    'matrix13': '#FFFF00',
    'matrix14': '#00FF41',
    'matrix15': '#E4D00A',
}

# Background color of the completion widget category headers.
c.colors.completion.category.bg = '#000000'

# Top/Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = '#C7C7C7'
c.colors.completion.category.border.top = '#C7C7C7'

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = '#C7C7C7'

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = '#000000'

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = '#000000'

# Text color of the completion widget.
c.colors.completion.fg = '#C7C7C7'

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = '#000000'

# Top/Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = '#C7C7C7'
c.colors.completion.item.selected.border.top = '#C7C7C7'

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = '#00F500'

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = '#00F500'

# Color of the scrollbar in completion view
c.colors.completion.scrollbar.bg = '#000000'

# Color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = '#000000'

# Background color for the download bar.
c.colors.downloads.bar.bg = '#00F500'

# Background color for downloads with errors.
c.colors.downloads.error.bg = '#FF0000'

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = '#C7C7C7'

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = matrix['matrix15']

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Background color for hints. Note that you can use a `rgba(...)` value
c.colors.hints.bg = matrix['matrix13']

# Font color for hints.
c.colors.hints.fg = matrix['matrix0']

# Font color for the matched part of hints.
c.colors.hints.match.fg = matrix['matrix10']

# Background color of the keyhint widget.
c.colors.keyhint.bg = matrix['matrix1']

# Text color for the keyhint widget.
c.colors.keyhint.fg = matrix['matrix5']

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = matrix['matrix13']

# Background color of an error message.
c.colors.messages.error.bg = '#FF0000'

# Border color of an error message.
c.colors.messages.error.border = '#FF0000'

# Foreground color of an error message.
c.colors.messages.error.fg = '#C7C7C7'

# Background color of an info message.
c.colors.messages.info.bg = matrix['matrix8']

# Border color of an info message.
c.colors.messages.info.border = matrix['matrix8']

# Foreground color an info message.
c.colors.messages.info.fg = matrix['matrix5']

# Background color of a warning message.
c.colors.messages.warning.bg = matrix['matrix12']

# Border color of a warning message.
c.colors.messages.warning.border = matrix['matrix12']

# Foreground color a warning message.
c.colors.messages.warning.fg = matrix['matrix5']

# Background color for prompts.
c.colors.prompts.bg = '#000000'

# Border used around UI elements in prompts.
c.colors.prompts.border = '1px solid ' + 'C7C7C7'

# Foreground color for prompts.
c.colors.prompts.fg = '#C7C7C7'

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = matrix['matrix3']

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = matrix['matrix15']

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = matrix['matrix5']

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = matrix['matrix15']

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = matrix['matrix5']

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = matrix['matrix2']

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = matrix['matrix5']

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = matrix['matrix2']

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = matrix['matrix5']

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = matrix['matrix14']

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = matrix['matrix1']

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = matrix['matrix0']

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = matrix['matrix5']

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = matrix['matrix10']

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = matrix['matrix5']

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = matrix['matrix3']

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = matrix['matrix5']

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = matrix['matrix5']

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = matrix['matrix11']

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = matrix['matrix5']

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = matrix['matrix8']

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = matrix['matrix5']

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = matrix['matrix14']

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = matrix['matrix12']

# Background color of the tab bar.
c.colors.tabs.bar.bg = '#000000'

# Background color of unselected even tabs.
c.colors.tabs.even.bg = '#000000'

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = '#C7C7C7'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = matrix['matrix11']

# Color gradient start for the tab indicator.
# c.colors.tabs.indicator.start = matrix['violet']

# Color gradient end for the tab indicator.
# c.colors.tabs.indicator.stop = matrix['orange']

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = '#000000'

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = '#C7C7C7'

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = '#000000'

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = '#00F500'

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = '#000000'

# Foreground color of selected 00F500odd tabs.
c.colors.tabs.selected.odd.fg = '#00F500'

# Background color for webpages if unset (or empty to use the theme's color)
c.colors.webpage.bg = 'black'
