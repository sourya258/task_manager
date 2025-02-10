

'''Failed in Iphone 16''' '''- whyyyy just this that's what
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to URL
url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7u4hn-a/p/itmc2732c112aeb1?pid=COMH64PYV3EVZZF8&lid=LSTCOMH64PYV3EVZZF83C6EE0&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=9e2a91ea-c6c2-41b7-b533-450770c84a6d.COMH64PYV3EVZZF8.SEARCH&ppt=hp&ppn=homepage&ssid=ewnwookzw00000001737303022140&qH=864faee128623e2f"
driver.get(url)

try:
    tag = driver.find_element(By.CSS_SELECTOR, '.col.pPAw9M')
    anchor = tag.find_elements(By.TAG_NAME,'a')
    time.sleep(2)
    
    anchor[-1].click()
    time.sleep(3)
    
except Exception as e:
    print(e)


try:
    page = 1
    while True:# Adjust page range as needed
          
        try:    
            # Scroll to bottom to load content
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Allow content to load

            # Wait for reviews to load
            reviews = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "col-9-12")]')) #DOjaWF gdgoEp col-9-12
                )

            if reviews:
                print(f"Found reviews on page {page} ")
                for idx, review in enumerate(reviews, start=1):
                    review_content = review.get_attribute("outerHTML")
                    with open(f"E:\\Coding\\Trials_Proj\\Iphone\\Macbook_Page{page}_Review.html", "w", encoding="utf-8") as f:
                        f.write(review_content + "\n")
            else:
                print(f"No reviews found on page ")
                break
                
                
        except Exception as e:
            print(f"An error occurred on page : {e}")
            print(traceback.format_exc())  # Print detailed error trace
            break
        
        try:
            first_loc = driver.find_element(By.CLASS_NAME, 'WSL9JP')
            second_loc = first_loc.find_elements(By.CLASS_NAME,'_9QVEpD')
            
            if len(second_loc) > 1:
                second_loc[1].click()
                url = 'https://www.flipkart.com' + second_loc[1].get_attribute('href')
                page += 1
            elif page == 1:
                second_loc[0].click()
                url = 'https://www.flipkart.com' + second_loc[0].get_attribute('href')
                page += 1
            else:break
            
                
        except Exception as e :
            print(e)
            break
            
finally:
    # Close the browser
    driver.quit()

'''
