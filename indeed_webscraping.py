from bs4 import BeautifulSoup
from requests import *
import pandas as pd
import time

#Declare Variables
max_pages = 2
curr_page = 0
num = 0
job_post = []

#Create Dataframe
list = ["Title", "Company", "Location", "Description", "Age","Hyperlink"]
indeedjobs_df = pd.DataFrame(data=job_post,columns=list)
variations = ["Data+scientist", "Web+developer"]

#Iterate through two different queries
for x in variations:
    #Iterate through number of pages
    for y in range(0,max_pages):

        #Change URL according to search query and page
        response = get("https://www.indeed.com/jobs?q="+x+"$40,000&l=Rockville+MD&sort=date&start="+str(curr_page))
        parsing = BeautifulSoup(response.text, "html.parser")
        results = parsing.find_all("div", class_="jobsearch-SerpJobCard")

        #Iterate through each job post
        for z in results:

            job_post.append([])
            # TITLE
            job_post[num].append(z.a.get("title").strip())

            # CITY
            job_post[num].append(z.find(["span","div"], class_="location").text.strip())

            # COMPANY
            job_post[num].append(z.find(["span","div"], class_="company").text.strip())

            # DESCRIPTION
            job_post[num].append(z.find(["span","div"], class_="summary").text.strip())

            # NUMBER OF DAYS
            try:
                job_post[num].append(z.find(["span","div"], class_="date").text.strip())

            except:
                job_post[num].append("N/A")
            # LINK
            job_post[num].append("https://www.indeed.com" + z.a.get("href").strip())

            #Copy ad info into dataframe
            indeedjobs_df.loc[num]=job_post[num]
            num = num + 1

            #Wait between queries
            time.sleep(1)

        curr_page = curr_page + 10

    curr_page = 0

#Convert dataframe into CSV
indeedjobs_df.to_csv("/Users/johnny/Desktop/414/indeed_web_scraping.csv", encoding="utf-8")
