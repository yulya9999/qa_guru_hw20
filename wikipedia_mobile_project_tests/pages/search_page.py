from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:

    def article_search(self, article):
        with step('Ввод названия статьи в поисковую строку'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
            browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(article)

        with step('Проверка результата поиска'):
            results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
            results.should(have.size_greater_than(0))
            results.first.should(have.text(article))

        with step('Клик по первой статье'):
            results.first.click()

        return self


search_page = SearchPage()
