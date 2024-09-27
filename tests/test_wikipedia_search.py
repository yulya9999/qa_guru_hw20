import allure
from wikipedia_mobile_project_tests.pages.search_page import search_page
from wikipedia_mobile_project_tests.pages.welcome_page import welcome_screen_page


@allure.feature("Поиск")
@allure.story("Успешный поиск статьи 'Python'")
def test_search_wikipedia_success():
    welcome_screen_page.welcome_screen_skip()
    search_page.article_search("Python")
    search_page.click_on_article()
