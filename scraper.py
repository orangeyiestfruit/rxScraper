import requests
from bs4 import BeautifulSoup
import io
from time import sleep
def makefile():
    with io.open("meds.txt", "w+", encoding="utf-8") as f1:
        with io.open("links.txt", "w+", encoding="utf-8") as f2:
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            for letter in alphabet:
                page = requests.get("https://www.rxlist.com/drugs/alpha_"+letter+".htm")
                soup = BeautifulSoup(page.content, 'html.parser')
                meds = soup.find('div',class_="contentstyle")
                children = meds.find_all("li")
                for x in children:
                    f2.write("https://www.rxlist.com/drugs/alpha_a.htm"+(x.find('a').get('href','') if x.find('a') else '')+"\n")
                    f1.write(x.get_text().replace("- FDA","").replace("- Multum","")+"\n")
    return 0
#print(makefile())

def getDiseases():
    with io.open("diseases.txt","w+",encoding="utf-8") as f1:
        page = requests.get("https://www.nhsinform.scot/illnesses-and-conditions/a-to-z")
        soup = BeautifulSoup(page.content, 'html.parser')
        diseases=soup.find_all('h2',class_="module__title")
        count=0
        for x in diseases:
            if count%2==1:
                f1.write(x.get_text().replace("        ","").replace("\n","",1).replace("    ",""))
            count+=1
def getGoogleInfo1():
    with io.open("descriptions1.txt","w+",encoding="utf-8") as f1:
        with io.open("diseases.txt", "r", encoding="utf-8") as f4:
            for line in f4:
                query1="https://bing.com/search?q="+line.replace(" ","%20").replace("\n","")
                page=requests.get(query1)
                soup = BeautifulSoup(page.content, 'html.parser')
                blegh=soup.find_all('div',class_="condAcc_para")
                count=0
                try:
                    blegh[0]=blegh[0]
                except:
                    f1.write("No information could be found on this disease - yet.\n")
                for x in blegh:
                    f1.write(x.get_text()+"\n")
                    count+=1
def getGoogleInfo2():
    dash=True
    with io.open("descriptions2.txt","w+",encoding="utf-8") as f2:
        with io.open("diseases.txt", "r", encoding="utf-8") as f4:
            for line in f4:
                f2.write("---")
                dash=True
                query1="https://bing.com/search?q="+line.replace(" ","%20").replace("\n","")
                page=requests.get(query1)
                soup = BeautifulSoup(page.content, 'html.parser')
                blegh=soup.find_all('div',class_="trt_list")
                try:
                    blegh[0]=blegh[0]
                except:
                    query1="https://bing.com/search?q="+line.replace(" ","%20").replace("\n","")
                    page=requests.get(query1)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    blegh=soup.find_all('div',class_="trt_list")
                count=-1
                for allah in blegh:
                    blagh = allah.find_all('div',class_='itemContent')
                    count+=1
                    for x in blagh:
                        f2.write(x.get_text()+"\n")
#getDiseases()
getGoogleInfo2()
