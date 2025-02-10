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
for page in range(1, 20):
    url = f"https://www.amazon.in/s?k=laptops&i=computers&rh=n%3A1375424031&page={page}&qid=1736960776&xpid=9x5mw5HGXik4p&ref=sr_pg_{page}"
    driver.get(url)
    time.sleep(3)  # Wait for the page to load completely

    # Scroll down to load all products
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Allow time for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract product details
    try:
        titles = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        if not titles:
            print(f"No products found on page {page}. Amazon might still be blocking automated access.")
        else:
            for i, title in enumerate(titles, start=1):
                data = title.get_attribute('outerHTML')  # Extract product title text
                with open(f'E:\\Coding\\data\\laptop_page_{page}_{i}.html', 'w', encoding='utf-8') as f:
                    f.write(data + '\n')
    except Exception as e:
        print(f"An error occurred on page {page}: {e}")

    time.sleep(5)  # Slow down scraping to reduce detection risk

# Close the browser
driver.quit()
