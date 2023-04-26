from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    PRICES = (By.CSS_SELECTOR, ".price-item.price-item--sale")

    def verify_filter_applied(self):
        all_prices = self.find_elements(*self.PRICES)
        first_price = all_prices[0].text.replace('Rs.', '')
        last_price = all_prices[-1].text.replace('Rs.', '')

        assert first_price < last_price, f'First price {first_price} is not lesser than the last price {last_price}'


