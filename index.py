from urllib.request import urlopen as get
from bs4 import BeautifulSoup as soup

class lvcalc:
    name=None
    result=None
    message=None

    def __init__(self,person1,person2):
        self.person1=person1
        self.person2=person2
        self.myurl= "http://lovecalculator.love/results/{}-and-{}".format(self.person1,self.person2)
        self.R_final()
    def req_page(self):
        page = get(self.myurl)
        page_content = page.read()
        page.close()
        page_html=soup(page_content,"html.parser")
        return page_html
    
    def get_name(self):
        w_page = self.req_page()
        container = w_page.body.section.findAll("div",{"id":"results"})
        conainer_name = container[0].findAll("p",{"id":"for-names"})
        try:
            name = conainer_name[0].text
        except:
            print("unable to extaract name")
        return name

    def get_result(self):
        w_page = self.req_page()
        container = w_page.body.section.findAll("div",{"id":"results"})
        conainer_res = container[0].findAll("p",{"id":"love-score"})
        try:
            score = conainer_res[0].text
        except:
            print("unable to extaract score")
        return score

    def get_message(self):
        w_page = self.req_page()
        container = w_page.body.section.findAll("div",{"id":"results"})
        conainer_msg = container[0].findAll("p",{"id":"love-message"})
        try:
            msg = conainer_msg[0].text
        except:
            print("unable to extaract score")
        return msg

    def R_final(self):
        # print("*********************************************************")
        # print("\t\t",self.get_name())
        # print("\t\t",self.get_result())
        # print("\t\t",self.get_message())
        # print("*********************************************************")
        self.name = self.get_name()
        self.result = self.get_result()
        self.message = self.get_message()  

"""while True:
    p1 = input("please insert your name:    ")
    p2 = input ("pleaser insert your crush name:    ")
    if " " in p1:
        p1 = p1[0:p1.index(" ")]
    if " " in p2:
        p2 = p2[0:p2.index(" ")]
    
    lvcalc(p1.strip(),p2.strip())"""
