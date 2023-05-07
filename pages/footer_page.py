from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class FooterPage(Page):
    FOOTER_SECTION = (By.CSS_SELECTOR, '.footer__content-top.page-width')
    FOOTER_LINKS = (By.CSS_SELECTOR, ".footer-block__details-content.list-unstyled a[href*=policies]")
    PAGE_HEADER = (By.XPATH, "//div[@class='shopify-policy__title']/h1")
    POLICIES = (By.XPATH, "//h2[contains(text(), 'Our policies')]")
    LINK_TEXT = ["Terms of service", "Refund policy", "Privacy policy", "Shipping policy"]

    def scroll_to_footer(self):
        self.click(*self.FOOTER_SECTION)

    def footer_links(self):
        all_links = self.find_elements(*self.FOOTER_LINKS)
        for i in range(len(all_links)):
            all_links = self.find_elements(*self.FOOTER_LINKS)
            self.driver.execute_script("arguments[0].scrollIntoView();", all_links[i])
            all_links[i].click()
            header = self.wait_for_element_appear(*self.PAGE_HEADER).text
            assert header in self.LINK_TEXT, f'Expected  Header not found but found {header}'
            self.driver.back()
            self.wait_for_element_click(*self.POLICIES)
            sleep(1)
