import allure

from wikipedia_mobile_project_tests.pages.welcome_page import welcome_screen_page


@allure.feature("Приветственное окно")
@allure.story("Проверка прохода по страницам")
def test_onboarding():
    welcome_screen_page.skip_onboarding()
