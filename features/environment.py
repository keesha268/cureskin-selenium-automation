from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    ##### FIREFOX ###########
    options = FirefoxOptions()
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    options.headless = True
    context.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    #########################


    #service = Service('/Users/keesh/cureskin-selenium-automation/chromedriver.exe')
    #context.driver = webdriver.Chrome(service=service)
    #context.browser = webdriver.Safari()
    #context.browser = webdriver.Firefox()
    #context.driver = webdriver.Firefox(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)

    # ## HEADLESS MODE ####
    # options = ChromeOptions
    # #options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    #
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service('/Users/keesh/cureskin-selenium-automation/chromedriver.exe')
    # )

    #context.driver.maximize_window()
    #context.driver.implicitly_wait(5)
    #context.driver.wait = WebDriverWait(context.driver, 10)
    #context.app = Application(context.driver)
    ## END HEADLESS MODE ####




# # for browerstack ###
#     # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#     bs_user = 'keeshaevanson_97eR4D'
#     bs_key = '7AawpyQyixpjZ7qyjeBs'
#
#     desired_cap = {
#         'browserName': 'Firefox',
#         'bstack:options': {
#             'os': 'Windows',
#             'osVersion': '10',
#             'sessionName': test_name
#         }
#     }
#     url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    #
    # context.app = Application(context.driver)






def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    #logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        # print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()