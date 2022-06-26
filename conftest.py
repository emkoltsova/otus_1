import logging
import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.1.100:9091/")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", default="192.168.1.100")
    parser.addoption("--bversion", action="store", default="100.0")


@pytest.fixture(scope='module')
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")

    logger = logging.getLogger('driver')
    test_name = request.node.name
    fh = logging.FileHandler('./test_opencart.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started!".format(test_name))

    if executor == "local":
        caps = {'goog:chromeOptions': {}}

        driver = webdriver.Chrome(
            executable_path=f"{os.path.expanduser('~/Downloads/drivers')}/chromedriver", desired_capabilities=caps
        )
    else:
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities={"browserName": browser, "browserVersion": version}
        )

    driver.test_name = test_name
    driver.log_level = log_level
    logger.info("Browser:{}".format(browser))

    driver.maximize_window()

    def open(path=""):
        logger.info("Opening url: {}".format(url + path))
        return driver.get(url + path)

    driver.open = open
    driver.open()

    def fin():
        driver.close()
        logger.info("===> Test {} finished!".format(test_name))

    request.addfinalizer(fin)

    return driver
