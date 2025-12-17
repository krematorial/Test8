from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    BOOKS_LINK = (By.LINK_TEXT, "Books")
    COMPUTERS_LINK = (By.LINK_TEXT, "Computers")
    PAGE_TITLE = (By.CLASS_NAME, "page-title")

    def navigate_to_books(self):
        self.click(self.BOOKS_LINK)

    def navigate_to_computers(self):
        self.click(self.COMPUTERS_LINK)

    def get_page_title(self):
        try:
            title_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.PAGE_TITLE)
            )
            return title_element.text.strip()
        except:
            return "Page title not found"
