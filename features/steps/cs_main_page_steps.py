from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Cureskin website')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Go to the footer section')
def scroll_to_footer(context):
    context.app.footer_page.scroll_to_footer()
    sleep(5)


@then('Click on each link and verify header')
def footer_links(context):
    context.app.footer_page.footer_links()
