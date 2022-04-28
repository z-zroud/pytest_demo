import pytest
import smtplib

@pytest.fixture(scope='module')
def smtp_connection():
    return smtplib.SMTP('www.baidu.com', 587, timeout=5)




def determine_scope(fixture_name, config):
    if config.getoption('--keep-containers', None):
        return 'session'
    return 'function'


# @pytest.fixture(scope=determine_scope)
# def docker_container():
#     yield spawn_container()