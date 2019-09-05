import sendmessage
from index import lvcalc as lv
p1=None
p2=None
def playee(msg,id):
    global p1
    global p2
    if msg == "/start":
        txt = "Hey Insert your name and your crush name separated by comma\n\tlike: someone,somebody or \n\t     someone father,somebody father"
        sendmessage.send(id,txt)
        return txt
    elif "," in msg:
        for i in msg:
            if i == " ":
                msg = msg.replace(i,"")
        p1=msg[0:msg.index(",")]
        p2=msg[msg.index(",")+1:]
        calc=lv(p1,p2)
        sendmessage.send(id,calc.name)
        sendmessage.send(id,calc.result)
        sendmessage.send(id,calc.message)
        txt = calc.name + "\n" + calc.result +"\n"+ calc.message+ "\n"
        return txt
    else:
        txt = "Incorrect input, please check again"
        sendmessage.send(id,txt)
        return txt


        