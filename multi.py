import hexchat
import time
__module_name__ = "multiload"
__module_version__ = "1.0"
__module_description__ = "a module to load/unload modules"

class nim:
    def __init__(a):
        a.nimmem = {}
        #print a
    def nimmove(s,a,b,c):
        #print a
        print s.nimmem          # uncomment to see memory
        name = a[0].split("!")[0][1:]
        if name in s.nimmem:
            try:
                go = int(a[3][1:])
                tmp = s.nimmem[name]
                tmp[0]+=s.test(go,tmp[2])
                rgo = s.test(go,tmp[2])
                if tmp[0] >= tmp[1]:
                    hexchat.command("msg "+name+" you've won nim, congratulations, we'll send the 1 million pounds when we get round to it (never)")
                    del s.nimmem[name]
                else:
                    comgo=s.test((tmp[1]-tmp[0])%(tmp[2]+1),tmp[2])
                    tmp[0]+=comgo
                    hexchat.command("msg "+name+" you played "+str(rgo)+" and I played "+str(comgo)+" which brought the total to "+str(tmp[0]))
                    if tmp[0] >= tmp[1]:
                        hexchat.command("msg "+name+" i win nim and I get 1 million pounds, bye")
                        del s.nimmem[name]
                    else:
                        s.nimmem[name] = tmp
            except:
                hexchat.command("msg "+name+" go must be an interger")
        else:
            if a[3][1:] == "setfirst":
                try:
                    s.nimmem[name] = a[4].split(",")
                    s.nimmem[name] = [0]+[int(s.nimmem[name][0])]+[int(s.nimmem[name][1])]
                    tmp=s.nimmem[name]
                    comgo=s.test((tmp[1]-tmp[0])%(tmp[2]+1),tmp[2])
                    tmp[0]+=comgo
                    hexchat.command("msg "+name+" I played "+str(comgo)+" which brought the total to "+str(tmp[0]))
                    if tmp[0] >= tmp[1]:
                        hexchat.command("msg "+name+" i win nim and I get 1 million pounds, bye")
                        del s.nimmem[name]
                    else:
                        s.nimmem[name] = tmp
                except:
                    hexchat.command("msg "+name+" setup must be valid")
                    del s.nimmem[name]
            elif a[3][1:] == "set":
                try:
                    #print( a[4][1] )
                    s.nimmem[name] = a[4].split(",")
                    #print s.nimmem[name]
                    s.nimmem[name] = [0]+[int(s.nimmem[name][0])]+[int(s.nimmem[name][1])]
                except:
                    hexchat.command("msg "+name+" setup must be valid")
                    del s.nimmem[name]
            else:
                hexchat.command("msg "+name+" welcome to the automated nim just privmsg me with a message in the format \"set 31(total limit),6(indlim)\" bye")
        return hexchat.EAT_NONE
    def test(s,a,b):
        a-=1
        a=a%b
        a+=1
        return a
def reply(a,b,c):
    hexchat.command("msg "+(a[0].split("!")[0][1:])+" the time is "+ time.ctime())
    #hexchat.command("msg "+(a[0].split("!")[0][1:])+" the time is 11:30")
    hexchat.prnt((a[0].split("@"))[-1])
    #hexchat.prnt(str(a)+str(b)+str(c))
    return hexchat.EAT_NONE
def chanreply(a,b,c):
    hexchat.command("msg #clock the time is "+ time.ctime())
    #hexchat.command("msg #clock the time is 11:30")
    hexchat.prnt((a[0].split("@"))[-1])
    #hexchat.prnt(str(a)+str(b)+str(c))
    return hexchat.EAT_NONE
def fizzbuzz(a,b,c):
    for i in range(1,100):
        if i%3:
            if i%5:
                hexchat.command("say "+str(i))
            else:
                hexchat.command("say fizzbuzz")
        else:
            if i%5:
                hexchat.command("say fizz")
            else:
                hexchat.command("say fizzbuzz")
    return hexchat.EAT_NONE
class loader:
    def __init__(s):
        s.fizz = False
        s.chan = False
        s.msg = False
        s.nim = False
    def on(s,a,b,c):
        if a[1] == "fizz":
            s.fizz = hexchat.hook_server("PRIVMSG",fizzbuzz)
            hexchat.prnt ("fizz on")
        elif a[1] == "chan":
            s.chan = hexchat.hook_server("JOIN",chanreply)
            hexchat.prnt ("chan on")
        elif a[1] == "msg":
            s.msg = hexchat.hook_server("PRIVMSG",reply)
            hexchat.prnt("msg on")
        elif a[1] == "nim":
            tmp=nim()
            s.nim = hexchat.hook_server("PRIVMSG",tmp.nimmove)
        else:
            hexchat.prnt("arguments must be valid")
        return hexchat.EAT_HEXCHAT
    def off(s,a,b,c):
        if a[1] == "fizz":
            hexchat.unhook(s.fizz)
            s.fizz = 0
        elif a[1] == "chan":
            hexchat.unhook(s.chan)
            s.chan = 0
        elif a[1] == "msg":
            hexchat.unhook(s.msg)
            s.msg = 0
        elif a[1] == "nim":
            hexchat.unhook(s.nim)
            s.nim = 0
        else:
            hexchat.prnt("args must be valid")
        return hexchat.EAT_HEXCHAT
load = loader()
hexchat.hook_command("on",load.on)
hexchat.hook_command("off",load.off)
hexchat.prnt("init")
