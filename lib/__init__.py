from .packages.selenium import webdriver
from .packages.selenium.webdriver import ChromeOptions
from .packages.selenium.webdriver.common.by import By
from .packages.selenium.webdriver.support.ui import WebDriverWait
from .packages.selenium.webdriver.support import expected_conditions as ec
from .packages.selenium_stealth import stealth


class Quote:
    def __init__(self) -> None:
        options = ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('--disable_extensions')
        options.add_argument('window-size=820,1180')
        options.add_argument('--incognito')
        options.add_argument('start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--disable-gpu')
        options.headless
        options.binary_location = '' #browser_path

        self.driver = webdriver.Chrome(options=options) #driver should be in the path

        self.driver.get('https://quotes-generator.com/quotes-generator.php')

    def get_quote(self, category: str):
        categories = self.driver.find_element(By.ID, 'header-gen-form').find_element(By.NAME, 'filter_category')\
                                                                       .find_elements(By.TAG_NAME, 'option')[1:]
        self.driver.find_element(By.ID, 'header-gen-form').find_element(By.NAME, 'filter_category')
        
        for x in categories:
            if x.text == category.capitalize():
                x.click()
                break
        else:
            return -1
        self.driver.find_element(By.CLASS_NAME, 'buttons').find_element(By.TAG_NAME, 'button').click()
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,'quote-box')))
        text = self.driver.find_element(By.CLASS_NAME, 'quote-box')
        text = text.find_element(By.CLASS_NAME, 'quote-text-1').text + '\n' + \
               text.find_element(By.CLASS_NAME, 'author').text
        return text.replace('™', '').replace('Â', '').replace('€', '')


    def __call__(self, category):
        return self.get_quote(category)

    
if __name__ == '__main__':
    quote = Quote()
    print(quote.get_quote('Sad'))
    print(quote.get_quote('Inspiration'))
