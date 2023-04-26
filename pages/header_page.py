from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class Header(Page):
    SORT_BY = (By.CSS_SELECTOR, 'span.button.button--secondary.button--small')
    LOW_TO_HIGH = (By.CSS_SELECTOR, "label[for='Filter-price-ascending-2']")

    def click_sort_by(self):
        self.click(*self.SORT_BY)
        self.click(*self.LOW_TO_HIGH)


