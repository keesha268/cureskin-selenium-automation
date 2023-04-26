from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SORT_BY = (By.CSS_SELECTOR, 'span.button.button--secondary.button--small')


@given('Open search results page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Select sort by price, high to low')
def click_sort_by(context):
    context.app.header.click_sort_by()
    sleep(5)


@then('Verify filter applied (fist product price should be > last product price)')
def verify_filter_applied(context, ):
    context.app.search_results_page.verify_filter_applied()