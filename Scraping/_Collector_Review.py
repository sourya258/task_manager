from bs4 import BeautifulSoup
import os
import pandas as pd

data = {'Name' : [], 'Buyer Status' : [], 'Ratings' : [], 'Review Title' :[], 'Review' : []}

for file in os.listdir('Project_Scraping_Reviews_Flipkart'):
    with open(f'E:\\Coding\\Project_Scraping_Reviews_Flipkart\\{file}', 'r', encoding='utf-8') as f:
        html_doc = f.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    # avg_stars =  soup.find('div', class_ = 'col-12-12 ggs1+C')
    # total_review_summary = soup.find('div', class_ ='col-8-12')
    # stars = total_review_summary.find('ul', class_ = 'lpANVI')     
    # rvw_rtld = total_review_summary.find('ul', class_ = '+psZUR')


    names = soup.find_all('p',class_ = '_2NsDsF AwS1CA')
    Buyer_qualif = soup.find_all('p', class_ = 'MztJPv')
    stars_rated = soup.find_all('div', class_ = 'XQDdHH Ga3i8K')
    reviews_titl = soup.find_all('p',class_ = 'z9E0IG')
    main_review = soup.find_all('div', class_ = 'ZmyHeo')

    
    for name, qualification, ratings, title, review in zip(names, Buyer_qualif, stars_rated, reviews_titl, main_review):
        data['Name'].append(name.get_text().strip())
        data['Buyer Status'].append(qualification.get_text().strip())
        data['Ratings'].append(ratings.get_text().strip())
        data['Review Title'].append(title.get_text().strip())
        data['Review'].append(review.get_text().replace('READ MORE','').strip())
        
df = pd.DataFrame.from_dict(data)
df.to_csv('Flipkart_Reviews_Scraped.csv')