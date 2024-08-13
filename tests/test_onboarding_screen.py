from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_onboarding():
    with step('Проверка первого экрана'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/option_label')).first.should(have.text('English'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Проверка второго экрана'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Проверка третьего экрана'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Проверка четвертого экрана'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
