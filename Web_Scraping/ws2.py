from bs4 import BeautifulSoup
import time
import requests # request information from web pages
# Import all job advertisement which main skill is python. Latest published
print('Write some skills you are not familiar with: ')
unfamiliar_skills = input('>')
print(f'Filtering out: {unfamiliar_skills}')
def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs= soup.find_all('div',class_='srp-job-bx')
    for index, job in enumerate(jobs):
        post_time= job.find('span',class_='posting-time').text
        if '1 ' in post_time:
            if not '11' in post_time:
                company_name= job.find('span',class_='srp-comp-name').text
                skills = job.find('div',class_='srp-keyskills').text.replace('\n','').replace(' ',', ')
                more_info = job.find('div',class_='srp-job-heading').a['href']
                if unfamiliar_skills not in skills:
                    with open(f'posts/{index}.txt','w') as f:
                        f.write(f'''
                        Company Name: {company_name}
                        Required Skills: {skills}
                        It was published: {post_time}
                        More Info: {more_info}''')
                    print(f'{index} file Saved.')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)