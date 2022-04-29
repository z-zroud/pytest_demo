from importlib_metadata import email
import pytest

from emaillib import Email, MailAdminClient


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    print('sending_user')
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    print('reciving_user')
    mail_admin.delete_user(user)


def test_mail_received(sending_user, receiving_user):
    email = Email(subject='Hey!', body="how's it going?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox