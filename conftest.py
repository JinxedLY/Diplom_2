import pytest
from stuff.helpers import RealHumans
from stuff.methods import Methods


@pytest.fixture
def user_make():
    user_payload = RealHumans.create_real_human()
    yield user_payload
    Methods.user_delete(user_payload)
