import pytest
import NanoSSO
from NanoSSO.exceptions import *


class TestNanoSSO:
    def test_init_no_params(self):
        """
        raise exception if params are not set
        """
        with pytest.raises(MissingAppConfig):
            NanoSSO.SSO(read_from_env_vars=True)

    def test_init_passed_params(self):
        s = NanoSSO.SSO(client_id='1 ', secret_key=' secret', callback='http://localhost/callback')
        assert s.client_id == '1'
        assert s.secret_key == 'secret'
        assert s.callback == 'http://localhost/callback'
        assert s.default_scopes == []
