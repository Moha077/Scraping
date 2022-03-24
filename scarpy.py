from pickle import TRUE
from bs4 import BeautifulSoup
import requests
import time

print('put some skill not want it')
unfim =input('>')
print(f'Filtiring out {unfim} ')

def fin_job():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup= BeautifulSoup(html_text,'lxml')
    jobs= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        publish=job.find('span',class_='sim-posted').span.text
        if 'few' in publish:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more=job.header.h2.a['href']
            if unfim not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company name : {company_name.strip()} \n')
                    f.write(f'Required Skills : {skills.strip()} \n')
                    f.write(f'More info : {more.strip()} \n')
                print(f'File saved: {index}')    
                
                
if __name__=='__main__':
    while True :
        fin_job()
        time_wait=10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait*60)







