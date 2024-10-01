import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import resource_id


class WelcomePage:
    def welcome_screen_skip(self):
        with allure.step('Пропустить приветственное окно'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_skip_button")).click()

        return self

    def click_continue_on_first_page(self):
        with allure.step('Нажатие кнопки "Continue" на первой странице'):
            browser.all((AppiumBy.ID, f'{resource_id}/option_label')).first.should(have.text('English'))
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
        return self

    def click_continue_on_second_page(self):
        with allure.step('Нажатие кнопки "Continue" на второй странице'):
            browser.element((AppiumBy.ID, f'{resource_id}/primaryTextView')).should(
                have.text('New ways to explore'))
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
        return self

    def click_continue_on_third_page(self):
        with allure.step('Нажатие кнопки "Continue" на третьей странице'):
            browser.element((AppiumBy.ID, f"{resource_id}/primaryTextView")).should(
                have.text('Reading lists with sync'))
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
        return self

    def click_continue_on_four_page(self):
        with allure.step('Нажатие кнопки "Get started" на четвертой странице'):
            browser.element((AppiumBy.ID, f"{resource_id}/primaryTextView")).should(have.text('Data & Privacy'))
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_done_button")).click()
        return self

    def skip_onboarding(self):
        self.click_continue_on_first_page()
        self.click_continue_on_second_page()
        self.click_continue_on_third_page()
        self.click_continue_on_four_page()
        return self

    # def welcome_screen(self):
    #     with allure.step('Нажатие кнопки "Continue" на первой странице'):
    #         browser.all((AppiumBy.ID, f'{resource_id}/option_label')).first.should(have.text('English'))
    #         browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
    #
    #     with allure.step('Нажатие кнопки "Continue" на второй странице'):
    #         browser.element((AppiumBy.ID, f'{resource_id}/primaryTextView')).should(
    #             have.text('New ways to explore'))
    #         browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
    #
    #     with allure.step('Нажатие кнопки "Continue" на третьей странице'):
    #         browser.element((AppiumBy.ID, f"{resource_id}/primaryTextView")).should(
    #             have.text('Reading lists with sync'))
    #         browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
    #
    #     with allure.step('Нажатие кнопки "Get started" на четвертой странице'):
    #         browser.element((AppiumBy.ID, f"{resource_id}/primaryTextView")).should(have.text('Data & Privacy'))
    #         browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_done_button")).click()
    #
    #     return self


welcome_screen_page = WelcomePage()
