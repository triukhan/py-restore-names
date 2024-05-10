import pytest
from app.restore_names import restore_names
from copy import copy


@pytest.fixture
def full_data():
    return [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy",}]


def test_without_first_name(full_data):
    copy_data = copy(full_data)
    del copy_data[0]["first_name"]
    restore_names(copy_data)
    assert copy_data == full_data


def test_with_none_first_name(full_data):
    copy_data = copy(full_data)
    copy_data[0]["first_name"] = None
    restore_names(copy_data)
    assert copy_data == full_data

