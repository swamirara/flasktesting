import requests
import pytest
from urllib.parse import urljoin

class TestApp():
    @classmethod
    def setup_class(self):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        self.base_url = "http://0.0.0.0:8081/"

    @classmethod
    def teardown_class(self):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """

    def test_users(self):
        users_url = urljoin(self.base_url, "admin/users")
        res = requests.get(users_url)
        assert res.ok == True
        assert res.json()["users"] is not None

    def test_groups(self):
        groups_url = urljoin(self.base_url, "admin/groups")
        res = requests.get(groups_url)
        assert res.ok == True
        assert res.json()["groups"] is not None
