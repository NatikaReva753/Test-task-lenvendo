from selenium import webdriver

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        self.wd.get("http://qa.digift.ru/")

    def find_element_by_xpath(self, xpath):
        return self.wd.find_element_by_xpath(xpath)

    def destroy(self):
        self.wd.quit()