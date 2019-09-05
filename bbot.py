
import requests
import json
import update as upp
import lv

offset=upp.rd_updd("update.txt")
timeout="99999999"
message=""
token = "https://api.telegram.org/bot*************************************/getupdates?"
r = None
cus_array=None
     
def requ():
    global r
    global token
    url=token+"offset={}".format(offset)+"&timeout={}".format(timeout)
    r = requests.get(url)
def logg_user(id,name,txt,replay):
        file = open("users_log.txt","a")
        file.write("=====================================\n")
        file.write("User-name: {}\n".format(name))
        file.write("Chat-id: {}\n".format(id))
        file.write("Message: {}\n".format(txt))
        file.write("Replay: {}\n".format(replay))
        file.write("=====================================\n")
        file.close()

def info():
        global cus_array
        name = cus_array["result"][0]["message"]["from"]["first_name"]
        text= cus_array["result"][0]["message"]["text"]
        if cus_array["result"][0]["message"]["chat"]["type"]=="private":
            id = cus_array["result"][0]["message"]["from"]["id"]
        elif cus_array["result"][0]["message"]["chat"]["type"]=="group":
            id = cus_array["result"][0]["message"]["chat"]["id"]
        info =[id,name,text]
        return info


def accept():
        global cus_array
        print("\tmessage arrived !!!!!")
        wrr()
        logs()
        infoo = info()
        print ("\t\t\tMessage:      {}".format(infoo[2]))
        print ("\t\t\tSender :      {}".format(infoo[1]))
        print ("\t\t\tID     :      {}".format(infoo[0]))
        print("\tReplaying........")
        try:
                replay = lv.playee(infoo[2],infoo[0])
                logg_user(infoo[0],infoo[1],infoo[2],replay)
        except:
                logg_user(infoo[0],infoo[1],infoo[2],"no replay")

        
    


def wrr():
    file=open("message.txt","a")
    file.write(message)
    file.write("\n")
    file.close()

def logs():
    global offset
    upp.loging("botlog.txt","update.txt")
    offset = str(int(offset)+1)
    upp.wr_updd("update.txt",offset)

def get_message():
    global cus_array
    global message
    global offset
    print("\t***************************************************************************************")
    print("\tRequesting url .......")
    print ("\tPlease wait until message arives (offset={})........".format(offset))
    requ()
    cus_array=json.loads(r.content)
    try:
        message=cus_array["result"][0]["message"]["text"]
        if message is not "":
            accept()
            print("\n\t***************************************************************************************")
    except:
        print("\n\tRetrying ..........")
        get_message()

while True:
        try:
                get_message()
        except RecursionError:
                get_message()
        except:
                get_message()
        finally:
                get_message()
