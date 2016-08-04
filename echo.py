import hexchat
import time
__module_name__ = "auto reply"
__module_version__ = "1.0"
__module_description__ = "a program to automaticly reply to privmsgs"
privm=0
def reply(a,b,c):
    hexchat.command("msg "+(a[0].split("!")[0][1:])+" the time is "+ time.ctime())
    #hexchat.command("msg "+(a[0].split("!")[0][1:])+" the time is 11:30")
    hexchat.prnt((a[0].split("@"))[-1])
    #hexchat.prnt(str(a)+str(b)+str(c))
    return hexchat.EAT_NONE
privm = hexchat.hook_server("privmsg",reply)
hexchat.prnt("hello")
