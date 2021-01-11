import requests
from bs4 import BeautifulSoup
payload = {
    '__EVENTTARGET':'ctl00$ContentPlaceHolder1$btnSend',
    '__EVENTARGUMENT':' ',
    '__VIEWSTATE':'1E70iLn2fBX/cMknEhbZa2SBTEvCvqDQjvp/jciRe1bLBmAsxhLia9q5IildeM8wdNVlEJ1J3s6piAJa4JDeF+zUjc4x7QvgjBXmhFBiNHx/ePN3MH8hi+d4NGYGOaGcFZDIQA==',
    '__VIEWSTATEGENERATOR':'9A093EFF',
    'q':'站內搜尋',
    'ctl00$ContentPlaceHolder1$txtQuery1':'物流單號'

    
}

res = requests.post("https://www.t-cat.com.tw/Inquire/Trace.aspx", data = payload)




soup = BeautifulSoup(res.text, "html.parser")
results = soup.find("td", "style1")
#print(results.select_one("strong"))
logistic_result = results.select_one("strong")

print(logistic_result.text)
