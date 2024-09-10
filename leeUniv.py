from urllib.request import urlopen
from bs4 import BeautifulSoup
from email import *

def extract_data():
    hangyang = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio11640371.html'
    
    result = urlopen(hangyang)
    html = result.read()
    
    soup = BeautifulSoup(html, 'html.parser')

    targets = ['독어독문학과', '사학과', '철학과', '정치외교학과', '사회학과', '관광학부', '교육학과', 
               '교육공학과', '국어교육과', '영어교육과', '관광학부', '정책학과', '경제금융학부', '경영학부', '국제학부']

    data = []
    
    for target in targets:
        tr = soup.find('td', text=target)
        
        if tr:
            tds = tr.parent.find_all('td')
            row_data = [td.text.strip() for td in tds]
            data.append(row_data)
    
    email_content = ""
    for row in data:
        if len(row) == 5:  
            department = f"{row[0]} {row[1]}"
            quota, applicants, rate = row[2], row[3], row[4]
        else:
            department = row[0]
            quota, applicants, rate = row[1], row[2], row[3]
        email_content += f"{department} | 모집인원 : {quota}명 | 지원인원 : {applicants}명 | 경쟁률 -> {rate}\n"
    
    return email_content