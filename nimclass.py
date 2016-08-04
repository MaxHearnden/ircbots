import hexchat
__module_name__ = "nim"
__module_version__ = "1.1"
__module_description__ = "nim bot"
class nim:
    def __init__(a):
        a.nimmem = {}
        #print a
    def nimmove(s,a,b,c):
        #print a
        name = a[0].split("!")[0][1:]
        if name in s.nimmem:
            try:
                go = int(a[3][1:])
                tmp = s.nimmem[name]
                tmp[0]+=s.test(go,tmp[2])
                if tmp[0] >= tmp[1]:
                    hexchat.command("msg "+name+" you've won nim, congratulations, we'll send the 1 million pounds when we get round to it (never)")
                    del s.nimmem[name]
                else:
                    comgo=s.test((tmp[1]-tmp[0])%(tmp[2]+1),tmp[2])
                    tmp[0]+=comgo
                    hexchat.command("msg "+name+" you played "+str(go)+" and I played "+str(comgo)+" which brung the total to "+str(tmp[0]))
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
                    hexchat.command("msg "+name+" I played "+str(comgo)+" which brung the total to "+str(tmp[0]))
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
                hexchat.command("msg "+name+" welcome to the autoated nim just privmsg me with a message in the format \"set 31(total limit),6(indlim)\" bye")
        return hexchat.EAT_NONE
    def test(s,a,b):
        a-=1
        a=a%b
        a+=1
        return a
tmp = nim()
hexchat.hook_server("privmsg",tmp.nimmove)
