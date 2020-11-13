#!/usr/bin/env python
from i3ipc import Connection
from notify2 import Notification, init
from psutil import Process

# This script only works with 'real' local terminals within Sway.
# We need to gracefully exit if using ssh, local console or a multiplexer.

multiplexers = ("tmux: server", "screen")

# determine if we can connect to ipc and get status
try:
    i3 = Connection()
# we won't get a status over ssh, via local console or not running i3/Sway
except Exception:
    exit()

# verify if running Sway
if "sway" not in i3.socket_path:
    exit()

p = Process()
# I am sure there is a better way to loop through all the parent processes
# names and make sure they aren't a multiplexer
for parent in p.parents():
    if parent.name() in multiplexers:
        exit()

# get terminal pid
terminal_pid = p.parents()[-2].pid

# get Sway's information on terminal
container = i3.get_tree().find_by_pid(terminal_pid)[0]

if not container.focused:
    # the application name is handled differently for wayland and xwayland
    # wayland
    if container.app_id:
        termial = container.app_id
    # xwayland
    elif container.window_instance:
        termial = container.window_instance
    # pretty sure this fallback is unneeded but leaving this for now
    else:
        termial = "terminal"

    init("sway-terminal-notify")
    n = Notification(
        "{} finished".format(termial),
        "on workspace {}".format(container.workspace().name),
        "/usr/share/icons/breeze/apps/48/utilities-terminal.svg",
    )
    n.show()
