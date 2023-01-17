from bs4 import BeautifulSoup
import requests 
import pandas as pd  
company = []
for i in range(1,10):
    url = f"http://www.bgapmea.org/index.php/member/member_details/{i}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', class_="content_main")

    for list in lists:  
        body = list.find_all("tr")
        company_name = body[0].find('h2').text
        director_name= body[1].find('h2').text
        company_address= body[2].find('h2').text
        factory_address= body[3].find('h2').text
        phone_number= body[4].find('h2').text
        fax_number= body[5].find('h2').text
        email_address= body[6].find('h2').text
        website= body[7].find('h2').text
        products= body[8].find('h2').text
        
        company.append([company_name, director_name, company_address, factory_address, phone_number,fax_number, email_address, website, products ])
        print(company)

    df = pd.DataFrame(company, columns=['Company Name', 'Director Name', 'Company Address',
    'Factory Address', 'Phone Number', 'Fax Number', 'Email Address', 'Website', 'Products'])
    df.to_csv('Company-details.csv')
    
    