import allure

from wikipedia_mobile_project_tests.pages.welcome_page import welcome_screen_page


@allure.feature("Приветственное окно")
@allure.story("Проверка прохода по страницам")
def test_onboarding():
    welcome_screen_page.skip_onboarding()
    welcome_screen_page.click_button_get_started()
    welcome_screen_page.check_text_welcome_page()
