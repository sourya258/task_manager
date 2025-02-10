from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options to avoid detection
options = Options()
options.add_argument("--headless")  # Run in headless mode (no browser UI)
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
options.add_argument("--disable-infobars")  # Remove "Chrome is being controlled by automated software"
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Custom headers to mimic a real browser
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Enable DevTools Protocol to set headers
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": custom_headers})

# Scrape Amazon for multiple pages

url = f"https://www.amazon.in//Dell-Alienware-i9-13980HX-Processor-Metallic/dp/B0C9F1VXCJ/ref=sr_1_242?dib=eyJ2IjoiMSJ9.R1w_kvShc95WCZ3-1QEKZKvY8zCD7T0AH3mGiFXO3TJzAGX46RXykyVn66T9CYZp-uZ8AmrgIIRLEQhjx1-t7PW3fF5ZSikFcftUO9AsR-JZBPZfoIu31RNeovPy7eont-0BKsoyQrrKq-8Nhb09YDepcwgVpV0KnsyatNL5Npr1oeIq_62ICcPkXHIV0mwtrPPa3gLaE7He8TCLpWMJC1AY0wilSBXKk2zoc7IApMdRdka93JzRJxmIskppy_D4v4dP9PAnmRML0jobB3ohf5uQwx0JZt4HkrEpPXfM5l7GwN7e1lTuFx6av_U7Fr82GRUM8RPa09js9foJPaWiaNo_8Rd2-nXrvrZMrxOhuxM.khsoJDiyaX7JC7dvxpZq7hGH2GQbCySFdgTyyrIac9s&dib_tag=se&keywords=laptops&qid=1736962375&s=computers&sr=1-242&xpid=9x5mw5HGXik4p]"
driver.get(url)
time.sleep(3)  # Wait for the page to load completel

# Extract product details
try:
    titles = driver.find_element(By.ID, "reviews-medley-footer")
    target = titles.find_element(By.LINK_TEXT, 'See more reviews')
    target.click()
        
except Exception as e:
    print(f"An error occurred on page")
    
driver.implicitly_wait(10)
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)

targewt_elem = driver.find_elements(By.CLASS_NAME, 'a-size-base review-title a-text-bold')
for i in targewt_elem:
    print(i.get_attribute('outerHTML'))

# Close the browser
driver.quit()
