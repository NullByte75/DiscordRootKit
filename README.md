# DiscordRootKit
a malware that hides itself in Discord's core files to get undetected
# How does it work?
Discord usually has file integrity checks for it's files, except for the index.js in the core, so i took advantage of it
# What does it do?
First, checks if the victim has been infected before, if it wasn't it copies itself to the startup folder, then changes the core file and adds a reverse shell on it
# Setup
Change the IP Address at line 18
# How can i see if i'm infected?
Normally, the Discord's index.js file (C:\Users\USERNAME\AppData\Roaming\discord\0.0.309\modules\discord_desktop_core\index.js) has only 1 line in it, that is:module.exports = require('./core.asar'); if the file has more than that, you might want to reinstall discord

#I DON'T TAKE RESPONSABILITY OF THE USE OF THIS TOOL!
