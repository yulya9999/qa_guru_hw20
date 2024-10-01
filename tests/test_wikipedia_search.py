import allure
import pytest

from wikipedia_mobile_project_tests.pages.search_page import search_page
from wikipedia_mobile_project_tests.pages.welcome_page import welcome_screen_page


@allure.feature("Поиск")
@allure.story("Успешный поиск статьи 'Python'")
@pytest.mark.parametrize("article", ["Python"])
def test_search_wikipedia_success(article):
    welcome_screen_page.welcome_screen_skip()
    search_page.article_search(article)
    search_page.click_on_article()
