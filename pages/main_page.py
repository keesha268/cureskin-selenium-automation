from pages.base_page import Page


class MainPage(Page):

    def open_main(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def open_main_page(self):
        self.open_url('https://https://shop.cureskin.com/')



