from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    # Software that takes input data and builds a structure, this case
    # takes string
    soup = BeautifulSoup(content,'lxml')
    #prettify method gives a cleaner version of the html
    #print(soup.prettify())
    # find method searchs for the first tag and stops running
    #tags = soup.find('h5')
    #courses_html_tags = soup.find_all('h5') # Creates a list of tags
    #for course in courses_html_tags:
    #    print(course.text) # takes the text of the tags
    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        # h5 methos gives h5 tags
        #print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
