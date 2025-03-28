import subprocess
from urllib.request import urlopen
import os

#  ██████╗ ██╗   ██╗████████╗███████╗
# ██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║   ██║██║   ██║   ██║   █████╗
# ██║▄▄ ██║██║   ██║   ██║   ██╔══╝
# ╚██████╔╝╚██████╔╝   ██║   ███████╗
#  ╚══▀▀═╝  ╚═════╝    ╚═╝   ╚══════╝

# Simone Gentili (gensimone)

# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Wheter to load autoconfig.yml or not.
config.load_autoconfig(False)

# Render all web contents using a dark theme.
config.set("colors.webpage.darkmode.enabled", True)

# Which method of blocking ads should be used.
# Valid values:
#   auto: Use Brave’s ABP-style adblocker if available, host blocking otherwise
#   adblock: Use Brave’s ABP-style adblocker
#   hosts: Use hosts blocking
#   both: Use both hosts blocking and Brave’s ABP-style adblocker
config.set("content.blocking.method", "both")

# Always restore open sites when qutebrowser is reopened.
config.set("auto_save.session", True)

# When to show the tab bar:
# Possible values: always, never, multiple, switching.
config.set("tabs.show", "multiple")

# Backend to use to display websites
config.set("backend", "webengine")

# Require a confirmation before quitting the application.
# Valid values:
#   always
#   multiple-tabs
#   downloads
#   never
# FIXME: use ConfirmQuit.downloads
# config.set("confirm_quit", "downloads")

# When to show a changelog after qutebrowser was upgraded.
# Valid values:
#   major: Show changelog for major upgrades (e.g. v2.0.0 → v3.0.0).
#   minor: Show changelog for major and minor upgrades (e.g. v2.0.0 → v2.1.0).
#   patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 → v2.0.1).
#   never: Never show changelog after upgrades.
config.set("changelog_after_upgrade", "patch")

# Default font family to use
c.fonts.default_family = 'DejaVuSansM Nerd Font'

# Default font size to use
c.fonts.default_size = '12pt'

# Web pages font size
c.fonts.web.size.default = 20
# c.fonts.web.size.default_fixed = 16
# c.fonts.web.size.minimum = 16
# c.fonts.web.size.minimum_logical = 16

# Web pages font type
c.fonts.web.family.cursive = "DejaVuSansM Nerd Font"
c.fonts.web.family.fantasy = "DejaVuSansM Nerd Font"
c.fonts.web.family.fixed = "DejaVuSansM Nerd Font"
c.fonts.web.family.sans_serif = "DejaVuSansM Nerd Font"
c.fonts.web.family.serif = "DejaVuSansM Nerd Font"
c.fonts.web.family.standard = "DejaVuSansM Nerd Font"

# Urls
# Page(s) to open at the start.
config.set("url.start_pages", [ "https://start.duckduckgo.com" ])
# Search engines which can be used via the address bar
config.set("url.searchengines", {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "pkg": "https://voidlinux.org/packages/?arch=x86_64&q={}",
    "yt": "https://youtube.com/results?search_query={}",
    "pb": "https://thepiratebay.org/search/{}"
})

config.source('colorscheme.py')

# # Xresources
# def read_xresources(prefix):
#     """
#     read settings from xresources
#     """
#     props = {}
#     x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE)
#     lines = x.stdout.decode().split("\n")
#     for line in filter(lambda l: l.startswith(prefix), lines):
#         prop, _, value = line.partition(":\t")
#         props[prop] = value
#     return props
#
# xresources = read_xresources("*")
# c.colors.statusbar.normal.bg = xresources["*.background"]
# c.colors.statusbar.command.bg = xresources["*.background"]
# c.colors.statusbar.command.fg = xresources["*.foreground"]
# c.colors.statusbar.normal.fg = xresources["*.foreground"]
#
# c.colors.tabs.even.bg = xresources["*.background"]
# c.colors.tabs.odd.bg = xresources["*.background"]
# c.colors.tabs.even.fg = xresources["*.foreground"]
# c.colors.tabs.odd.fg = xresources["*.foreground"]
# c.colors.tabs.selected.even.bg = xresources["*.color8"]
# c.colors.tabs.selected.odd.bg = xresources["*.color8"]
# c.colors.hints.bg = xresources["*.background"]
# c.colors.hints.fg = xresources["*.foreground"]
#
# # change title format
# c.tabs.title.format = "{audio}{current_title}"
#
# c.colors.tabs.indicator.stop = xresources["*.color14"]
# c.colors.completion.odd.bg = xresources["*.background"]
# c.colors.completion.even.bg = xresources["*.background"]
# c.colors.completion.fg = xresources["*.foreground"]
# c.colors.completion.category.bg = xresources["*.background"]
# c.colors.completion.category.fg = xresources["*.foreground"]
# c.colors.completion.item.selected.bg = xresources["*.background"]
# c.colors.completion.item.selected.fg = xresources["*.foreground"]
#
# If not in light theme
# if xresources["*.background"] != "#ffffff":
#     # c.qt.args = ['blink-settings=darkMode=4']
#     # c.colors.webpage.prefers_color_scheme_dark = True
#     c.colors.webpage.darkmode.enabled = True
#     c.hints.border = "1px solid #FFFFFF"

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:133.0) Gecko/20100101 Firefox/133.0', 'https://accounts.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow locally loaded documents to access remote URLs.
# Type: Bool
config.set('content.local_content_can_access_remote_urls', True, 'file:///home/void/.local/share/qutebrowser/userscripts/*')

# Allow locally loaded documents to access other local URLs.
# Type: Bool
config.set('content.local_content_can_access_file_urls', False, 'file:///home/void/.local/share/qutebrowser/userscripts/*')
