#Author: Chatchawal Sangkeettrakarn
#Date: September 20,2020.

from typing import Counter
from fastapi import FastAPI
import uvicorn
import numpy as np
import re
import requests
import math
import sqrt
from bs4 import BeautifulSoup
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/nun")
def nun():
    return 'Hello nun'

def result(res):
    return {"result":res}

@app.get("/")
async def main():
    return 'Hello World'

@app.get("/test")
async def test():
    return 'Test Tutorial'

#ส่งงาน
@app.get("/Assignment_add")
async def add(a: int = 2343240987, b: int = 20034932):
    return a+b

#ส่งงาน 2 with จ๋า อุ้ม
@app.get("/assignment_2")
Counter = 0
total = 0
while Counter < 10:
    total += Counter
    Counter += 1
print(total)

#ส่งงาน 2 
#@app.get("/how_to_find_pythagorean")
#from math import sqrt

#print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
#formula = input('Which side (a, b, c) do you wish to calculate? side> ')

#if formula == 'c':
	side_a = int(input('Input the length of side a: '))
	side_b = int(input('Input the length of side b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('The length of side c is: ' )
	print(side_c)

#elif formula == 'a':
    #side_b = int(input('Input the length of side b: '))
    #side_c = int(input('Input the length of side c: '))
    
    #side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    #print('The length of side a is' )
    #print(side_a)

#elif formula == 'b':
    #side_a = int(input('Input the length of side a: '))
    #side_b = int(input('Input the length of side c: '))
        
    #side_c = sqrt(side_c * side_c - side_a * side_a)
    
    #print('The length of side b is')
    #print(side_c)

#else:
	#print('Please select a side between a, b, c')#/


@app.get("/add")
async def add(a: int = 0, b: int = 0):
    return a+b

@app.get("/mul")
async def mul(a: int = 0, b: int = 0):
    return a*b

@app.get("/pow")
async def pow(a: int = 0, b: int = 0):
    return math.pow(a,b)


def tonumlist(li):
    ls = li.split(',')
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return list(ls)

@app.get("/asc")
async def asc(li):
    ls = tonumlist(li)
    ls.sort()
    return ls

@app.get("/desc")
async def desc(li):
    ls = tonumlist(li)
    ls.sort(reverse=True)
    return ls

@app.get("/sum")
async def sum(li):
    ls = tonumlist(li)
    return np.sum(np.array(ls))

@app.get("/avg")
async def avg(li):
    ls = tonumlist(li)
    return np.average(ls)

@app.get("/mean")
async def mean(li):
    ls = tonumlist(li)
    return np.mean(ls)

@app.get("/max")
async def max(li):
    ls = tonumlist(li)
    return np.amax(ls)

@app.get("/min")
async def min(li):
    ls = tonumlist(li)
    return np.amin(ls)

@app.get("/validation-ctzid")
async def validation_ctzid(text):
    if(len(text) != 13):
        return False
    
    sum = 0
    listdata = list(text)
    
    for i in range(12):
        sum+=int(listdata[i])*(13-i)

    d13 = (11-(sum%11))%10
        
    return d13==int(listdata[12])

@app.get("/validation-email")
async def validation_email(text):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex,text):
        return True
    else:
        return False
    
    
@app.get("/google-search",response_class=PlainTextResponse)
def google_search(text):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    url = 'https://www.google.com/search?q=' + str(text)
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    t = soup.findAll('div', {'class':"r"})
    i = 0
    result = ''
    for a in t:
        href = a.a['href']
        head = a.h3.text
        result = result + head + '<br>' + href + '<br><br>'
        i += 1
        if(i >= 5):
            break
    
    return(result)




if __name__ == '__main__':
   uvicorn.run(app, host="0.0.0.0", port=80, debug=True) 