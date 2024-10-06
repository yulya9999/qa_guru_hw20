import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import resource_id


class WelcomePage:
    def welcome_screen_skip(self):
        with allure.step('Пропустить приветственное окно'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_skip_button")).click()
        return self

    def skip_onboarding(self):
        with allure.step('Нажатие кнопки "Continue" на страницах диалогового окна'):
            for _ in range(3):
                browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
        return self

    def accept_eula(self):
        with allure.step('Нажатие кнопки "Get started"'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_done_button")).click()
        return self

    def check_text_welcome_page(self):
        with allure.step('Проверка перехода на главный экран'):
            (browser.element((AppiumBy.ID, f"{resource_id}/view_announcement_text"))
             .should(have.text('Customize your Explore feed')))
        return self


welcome_screen_page = WelcomePage()
