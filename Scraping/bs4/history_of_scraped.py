# '''BBT'''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# url = 'https://www.bigboytoyz.com/collection'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# try:
#     result = requests.get(url, headers=headers, timeout=10)
#     result.raise_for_status()  # Raise an error for bad HTTP responses (4xx, 5xx)
#     soup = BeautifulSoup(result.text, 'html.parser')
# except requests.exceptions.RequestException as e:
#     print(f"Error fetching the URL: {e}")
    
# text = soup.find('div', class_ = 'middle-cntnr')
# infos = text.select('span.cntnt-grp')

# data = {'Name':[], 'Price' : [], 'Emi Price': [], 'Registration Year': [], 'Kms Driven' : [], 'Fuel Type': [], 'Registration States': []}

# for info in infos:
#     name = info.find('h6')
#     data['Name'].append(name.get_text().strip())
    
#     price = info.find('p')
#     data['Price'].append(price.get_text().strip())
    
#     emi_price = info.find('span',class_ = 'emiprice')
#     data['Emi Price'].append(emi_price.get_text().replace("EMI STARTS @ ", "").strip())
    
#     regd_yr = info.find('li', class_ = 'model')
#     data['Registration Year'].append(regd_yr.get_text().replace("Reg. Year", "").strip())

#     kms_driven = info.find('li', class_ ="kms") 
#     data['Kms Driven'].append(kms_driven.get_text().replace('KMS','').strip())
    
#     fuel_type = info.select_one('li.fueltype :nth-of-type(2)')
#     data['Fuel Type'].append(fuel_type.get_text().strip())
    
#     regd_states = info.select_one('li.fueltype:nth-of-type(4)')
#     if regd_states is not None:
#         data['Registration States'].append(regd_states.get_text().replace('Reg. State','').strip())  
#     else:
#         data['Registration States'].append('No info')
        
# df = pd.DataFrame.from_dict(data)
# df.to_csv('Data4.csv', index=False)
    

'''Job Site'''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35&clusterName=CLUSTER_FA&hc=CLUSTER_FA"
# result = requests.get(url)

# data = {'Title' : [], "Company" : [], "Posted" : [], "Description" : [], "More Skills" : [], "Locations" : [], "Experience" : [], "Salary" : []}
# soup = BeautifulSoup(result.text, "html.parser")
# texts = soup.find("ul", class_="new-joblist")

# titl = texts.select("h2.heading-trun")
# companies = texts.select("h3.joblist-comp-name")
# posted = texts.select("span.sim-posted")
# description = texts.select("li.job-description__")
# more_skills = texts.find_all("div",class_ = "more-skills-sections")
# locations = texts.find_all("li", class_ = "srp-zindex location-tru")
# experiences = texts.find_all("ul", class_ ="top-jd-dtl mt-16 clearfix")





# for tit, company, post, describe, more_skill, location,  in zip(titl,companies,posted,description, more_skills, locations):
#     skill_list = []
#     data['Title'].append(tit['title'].strip(" "))
#     data["Company"].append(company.get_text().strip())
#     data["Posted"].append(post.get_text().strip())
#     data["Description"].append(describe.get_text().strip())
#     data["Locations"].append(location.get_text().strip())
#     for child in more_skill.children:
#           skill_list.append(child.get_text().strip())
#     data["More Skills"].append(','.join(skill_list).removeprefix(",").replace(",,",","))
    


# for pre_li_experience in experiences:
#     with_li_experience = pre_li_experience.find_all("li")
#     for the_exact_experience in with_li_experience:
#         if the_exact_experience.find("i", class_ = "srp-icons experience"):
#             data["Experience"].append(the_exact_experience.get_text())
              
            
# for pre_li_salary in experiences:
#     with_li_salary = pre_li_salary.find_all("li")
#     for the_exact_salary in with_li_salary:
#         if the_exact_salary.find("i", class_ = "srp-icons salary"):
#              data["Salary"].append(' '.join(the_exact_salary.get_text().split()))
        
       
# df = pd.DataFrame.from_dict(data)
# df.to_csv("data.csv", index=False)


'''BMW'''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import chardet

# url = "https://www.bmw.in/en/all-models.html?tl=grp-wdpl-bcom-mix-mn-.-nscf-.-.-"
# result = requests.get(url)

# detected_encoding = chardet.detect(result.content)
# result.encoding = detected_encoding['encoding']

# data = {"Name" : [], "Fuel" : [], "Prices":[], 'Details' : []}

# soup = BeautifulSoup(result.text, "html.parser")
# details = soup.find("div", class_ = "cmp-container", id = "container-3a47d09ad6")

# tags = details.find_all("h2", class_ = "cmp-modelselection__group-name")
# names = details.find_all("h5", class_ = "cmp-modelcard__name")
# fuel_types = details.find_all("div", class_ = "cmp-modelcard__fuel-type")
# prices = details.find_all("span", class_ = "cmp-modelcard__price")

# extra_details = soup.find("div", class_ = "ds2-cms-output ds2-table-element")



# for name, fuel_type, price in zip(names,fuel_types,prices): 
#     data['Name'].append(name.get_text().strip())   
#     data['Fuel'].append(fuel_type.get_text().strip()) 
#     cleaned_price = price.get_text().replace("\xa0", "").strip()
#     data['Prices'].append(cleaned_price) 
#     data['Details'].append(extra_details.get_text().strip())  

# df = pd.DataFrame.from_dict(data)
# df.to_csv("data2.csv", index=False)

'''Amazon Macbook'''
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# url ="https://www.amazon.in/s?k=macbook&crid=10WAGQE0CLMAM&sprefix=macboo%2Caps%2C275&ref=nb_sb_noss_2"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Connection": "keep-alive",
#     "Upgrade-Insecure-Requests": "1",
#     "TE": "Trailers"
# }
# main_url_data = requests.get(url, headers=headers)
# main_data = BeautifulSoup(main_url_data.text, "html.parser")

# import time
# time.sleep(2)
 


# data = {'Name' :[] , 'Current Price' : [], 'Previoius Price' : []}

# extracted_specific_data_pool = main_data.find("div", class_ = "sg-col-20-of-24 s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16")
# item_name = extracted_specific_data_pool.find_all("h2", class_ = "a-size-medium a-spacing-none a-color-base a-text-normal")
# item_current_price = extracted_specific_data_pool.find_all("span", class_ = "a-price-whole")
# item_previous_price = extracted_specific_data_pool.find_all("span", class_ = "a-price a-text-price")

# for pre_srch, price, bfr_srch_previous_price in zip(item_name,item_current_price,item_previous_price):
#     aftr_srch = pre_srch.find_all("span")
#     for exct_name in aftr_srch:
#         data['Name'].append(exct_name.get_text().strip())
#     data['Current Price'].append(price.get_text().strip())

            
            

     
# for bfr_srch_previous_price in item_previous_price:
#         aftr_srch_previous_price = bfr_srch_previous_price.find("span", class_ ="a-offscreen")
#         for previous_price in aftr_srch_previous_price:
#             # print(previous_price.get_text().strip())
#             data['Previoius Price'].append(previous_price.get_text().strip())
            
# df = pd.DataFrame.from_dict(data)
# df.to_csv("data3.csv", index=None)

    

        




    
        
    
    
    
    
    

    

    





