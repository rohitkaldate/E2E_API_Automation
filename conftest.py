from datetime import datetime
from distutils.command.config import config

import pytest
from requests import session


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/reports_{now}.html"

@pytest.fixture(scope='session',autouse=True)
def setup_teardown():
    print("*** Tests Started ***")
    yield
    print("*** Tests Completed ***")