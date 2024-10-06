import os

import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

import config
from wikipedia_mobile_project_tests.utils import attach, file

resource_id = os.getenv('RESOURCE_ID')


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = file.path_from_project(f".env.{context}")

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)
    browser.quit()
