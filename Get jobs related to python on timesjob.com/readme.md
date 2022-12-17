## Get latest job postings from timesjobs.com
---
###$ Instructions to execute 

###### 1. Install dependencies  
```
pip install BeautifulSoup4
pip install requests
pip install time
```
###### 2. Move to directory where main.py exist
###### 2. Run main.py
```python
python main.py
```
###$ Output
###### 1. open /posts/saved.txt file

---
###$ PythonCode

```python

from bs4 import BeautifulSoup
import requests
import time

urls = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

def findJobs():
  count=0
  html_text = requests.get(urls).text;
  soup = BeautifulSoup(html_text, 'lxml')

  jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

  with open(f'posts/saved.txt','w') as f:
   for index, job in enumerate(jobs):
    location = job.find('ul', class_="top-jd-dtl clearfix").span.text
    skills = job.find('ul', class_="list-job-dtl clearfix").span.text
    company = job.find('h3', class_="joblist-comp-name").text
    link = job.find('header', class_="clearfix").h2.a['href']
    
    if True:
        count+=1
        f.write(f"Company: {company.strip().replace('(More Jobs)','')}\n")
        f.write(f"Location: {location.strip()}\n")
        f.write(f"Skills: {skills.strip()}\n")
        f.write(f"Link: {link}\n\n")
  return count;
    
print(f'Fetching Data from\n{urls}\n.')
x = findJobs()
print(f'{x} new jobs updated.')

```
