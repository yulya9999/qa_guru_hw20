from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import resource_id


class SearchPage:

    def article_search(self, article):
        with step('Ввод названия статьи в поисковую строку'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, f"{resource_id}/search_src_text")).type(article)
        return self

    def click_on_first_article(self):
        with step('Клик по первой статье'):
            browser.all((AppiumBy.ID, f'{resource_id}/page_list_item_title')).first.click()
        return self

    def check_title(self, article):
        with step('Проверка заголовка статьи'):
            browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).first.should(have.text(article))
        return self


search_page = SearchPage()
