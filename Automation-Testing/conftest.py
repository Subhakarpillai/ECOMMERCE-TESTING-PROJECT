
import pytest
from selenium import webdriver

@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--incognito")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    yield browser

    browser.quit()
