# python-auto-login
a python script that will automatically ssh/telnet to a target device

## prerequisities
* linux, wsl
* bash, telnet, ssh, python3
* python pexpect module
* the mypyvars.py file with username and password defined (yeah i know :))

## usage
./autologin.pl [ip addr]

i created a command alias in .bashrc so i can exeucte with a short name

this app will ssh/telnet to your target device automatically and hand you back the keyboard. enjoy!
