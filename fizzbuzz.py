import hexchat
__module_name__ = "fizzbuzz"
__module_version__ = "1.0"
__module_description__ = "plays fizz buzz on command"

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
                hexchat.command("say fizzbuzz"))
    return hexchat.EAT_NONE
hexchat.hook_server("PRIVMSG",fizzbuzz)
print("init")
