## Sway terminal notify

Need an indication that some long running command finishes when the terminal no longer has focus?  In i3, I use the terminal's visual bell feature along with adding '\a' to `PS1` to mark the terminal as urgent.  In Sway, I had come up with this workaround as [Wayland does not yet support urgency hints][00].

- Install the [i3ipc][0], [notify2][1] and [psutil][2] Python modules along with [mako][3] notification daemon.

- Clone this repository or download sway-terminal-notify.py and make it executable.  

- Add `PROMPT_COMMAND='$(/path/to/sway-terminal-notify.py)'` to your .bashrc file or equivalent for other shells.

- Change the next to last line in sway-terminal-notify.py to use a different icon.  Add something like the following to the mako configuration to theme the alerts:

```dosini
[app-name="sway-terminal-notify"]
background-color=#000000
text-color=#00ff00
```

This workaround does not work with terminal multiplexers or ssh.  I prefer urgent windows to notifications for this reason and visually is cleaner.  To me, this looks better:

![urgent](https://i.imgur.com/zs9t7Fu.png)

Than this:

![notification](https://i.imgur.com/R5qKOVu.png)

I attempted to recreate a notification that would be just a small red box with the workspace number that would go over the workspace number in the status bar.  It appears that Sway or mako won't allow notifications to appear over the status bar.  

[00]: https://gitlab.freedesktop.org/wayland/wayland-protocols/-/merge_requests/9
[0]: https://pypi.org/project/i3ipc
[1]: https://pypi.python.org/pypi/notify2
[2]: https://pypi.org/project/psutil
[3]: https://github.com/emersion/mako
