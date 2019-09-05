#important libs for geting the html and for 
#making the DOM(document object model)an array of elements 
from urllib.request import urlopen as get
from bs4 import BeautifulSoup as soup

#important variables
person1=input("What is your Name:   ")
person2=input("What is your Name:   ")
myurl = "http://lovecalculator.love/results/{}-and-{}".format(person1,person2)

#creating connection and grabing all the data
page = get(myurl)
page_content = page.read()
page.close()

#making perfect html (prased html)

page_html=soup(page_content,"html.parser")

# now we have an array of html page
# and we access elements by page_arr.p
# page_html.div.body.p
# arr=page_html.findAll("element",{"attribute":"value"})
# that return array of all matched elements
# to find attributes : div.div.a.img["width"] or ["text"]

p1 = page_html.body.section.findAll("div",{"id":"results"})
first_line=p1[0].p.text
p2 =  page_html.body.section.findAll("div",{"id":"love-score"})
print(p2)