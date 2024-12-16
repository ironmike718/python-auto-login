#!/usr/bin/env python3

from mypyvars import *
import sys, pexpect

"""
date: 03.15.20
author: michael melendez
description: python script performs auto login to network devices via telnet & ssh
requires: telnet and ssh via terminal, credentials defined in mypyvars.py file with uname and pword variable names
execute: ./autologin.py <ip addr>
"""

def doTel(host):

    # attempt telnet connection

    sess = pexpect.spawn("/usr/bin/telnet", [host])
    #sess = pexpect.spawn("/usr/bin/bash", ["-c", "/usr/bin/telnet " + host + "| ct"])
    idx = sess.expect(["login:","Username:",pexpect.EOF,pexpect.TIMEOUT],timeout=4)

    if idx == 0 or idx == 1:
        res = 23
        sess.sendline(uname)
        sess.expect("Password:")
        sess.sendline(pword)
        sess.interact()
    else:
        res = 0
        print("\nError: Unable to connect to host %s via TELNET\n" % host)

    return res

def doSsh(host):

    # attempt ssh connection

    targ = "%s@%s" % (uname,host)
    sess = pexpect.spawn("/usr/bin/ssh", [targ])
    #sess = pexpect.spawn("/usr/bin/bash", ["-c", "/usr/bin/ssh " + targ + "| ct"])
    idx = sess.expect(["continue connecting","word:",pexpect.EOF,pexpect.TIMEOUT],timeout=4)

    if idx == 0:
        sess.sendline("yes")
        sess.expect("word:")
        sess.sendline(pword)
    elif idx == 1:
        sess.sendline(pword)
    else:
        sys.exit("\nError: Unable to connect to host %s via SSH\n" % host)

    sess.interact()

def main():

    # process host/ip arg

    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        sys.exit("\nError: Provide valid switch ip addr or hostname\n")

    conn = doTel(host)

    if conn != 23:
        doSsh(host)

if __name__ == '__main__':
    main()
