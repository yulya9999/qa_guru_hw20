import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import resource_id


class WelcomePage:
    def welcome_screen_skip(self):
        with allure.step('Пропустить приветственное окно'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_skip_button")).click()
        return self

    def check_text_welcome_page(self):
        with allure.step('Проверка перехода на главный экран'):
            (browser.element((AppiumBy.ID, f"{resource_id}/view_announcement_text"))
             .should(have.text('Customize your Explore feed')))
        return self

    def click_continue_on_dialog_box(self):
        with allure.step('Нажатие кнопки "Continue" в диалоговом окне'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_forward_button")).click()
        return self

    def choose_language(self, language):
        with allure.step('Выбор языка на первой странице диалогового окна'):
            browser.all((AppiumBy.ID, f'{resource_id}/option_label')).first.should(have.text(f'{language}'))
        return self

    def checking_text_on_dialog_pages(self, text):
        with allure.step('Проверка текста на странице диалогового окна'):
            browser.element((AppiumBy.ID, f'{resource_id}/primaryTextView')).should(
                have.text(f'{text}'))
        return self

    def accept_eula(self):
        with allure.step('Нажатие кнопки "Get started"'):
            browser.element((AppiumBy.ID, f"{resource_id}/fragment_onboarding_done_button")).click()
        return self

    def skip_onboarding(self):
        with allure.step('Первая страница'):
            self.choose_language('English')
            self.click_continue_on_dialog_box()
        with allure.step('Вторая страница'):
            self.checking_text_on_dialog_pages('New ways to explore')
            self.click_continue_on_dialog_box()
        with allure.step('Третья страница'):
            self.checking_text_on_dialog_pages('Reading lists with sync')
            self.click_continue_on_dialog_box()
        with allure.step('Четвертая страница'):
            self.checking_text_on_dialog_pages('Data & Privacy')
            self.accept_eula()
        return self


welcome_screen_page = WelcomePage()
