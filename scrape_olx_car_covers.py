from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv

def scrape_olx_car_covers(output_file='olx_car_covers.csv'):
   
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        url = "https://www.olx.in/items/q-car-cover"
        driver.get(url)
        time.sleep(5)  
        
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
       
        items = driver.find_elements(By.CSS_SELECTOR, 'li[data-aut-id="itemBox"]')
        
        results = []
        for item in items:
            title_el = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemTitle"]')
            price_el = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemPrice"]')
            location_el = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemLocation"]')
            link_el = item.find_element(By.CSS_SELECTOR, 'a')
            
            title = title_el.text.strip()
            price = price_el.text.strip()
            location = location_el.text.strip()
            link = link_el.get_attribute('href')
            
            results.append([title, price, location, link])
        
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Title', 'Price', 'Location', 'URL'])
            writer.writerows(results)
        
        print(f"Scraped {len(results)} items. Results saved in '{output_file}'.")
    
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_olx_car_covers()
