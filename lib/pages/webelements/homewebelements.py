
from selenium.webdriver.common.by import By


class HomeWebElements:

    signin_button = (By.CSS_SELECTOR, '#root .mc6t-main-content .wRhj-mod-justify-end div span div')
    title_h2 = (By.XPATH, "//h2[@class='AQWr-mod-margin-bottom-xlarge c0qPo']")
    start_date_div = (By.XPATH, "(//div[@role='button'])[10]")
    end_date_div = (By.XPATH, "(//div[@role='button'])[11]")
    search_button = (By.XPATH, "//button[@type='submit']")
    origin_input = (By.XPATH, "(//input[@type='text'])[2]")
    menu_button = (By.CSS_SELECTOR, '#root .mc6t-nav-button div')
    menu_selectors = {
        "flights": (By.XPATH, "//a[@href='/flights']"),
        "stays": (By.XPATH, "//a[@href='/stays']"),
        "cars": (By.XPATH, "//a[@href='/cars']"),
    }
