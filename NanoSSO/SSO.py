import os
from typing import Optional
from .exceptions import *


class SSO:
    """
    The SSO class for obtaining, managing, and validating authorization codes, access tokens, and refresh tokens with ESI.
    """
    def __init__(self, client_id: str = None, secret_key: str = None, callback: str = None,
                 default_scopes: Optional[list[str]] = None, read_from_env_vars: bool = False):
        """

        :param client_id:
        :param secret_key:
        :param callback:
        :param default_scopes:
        :param read_from_env_vars:
        """
        if default_scopes is None:
            self.scope = []

        self.client_id = str((client_id or (os.environ.get('NanoSSO_client_id', '') if read_from_env_vars else ''))).strip()
        self.secret_key = str((secret_key or (os.environ.get('NanoSSO_secret_key', '') if read_from_env_vars else ''))).strip()
        self.callback = str((callback or (os.environ.get('NanoSSO_callback', '') if read_from_env_vars else ''))).strip()
        self.default_scopes = default_scopes or (os.environ.get('NanoSSO_default_scopes', '').split(' ') if read_from_env_vars else [])

        if not self.client_id:
            if read_from_env_vars:
                raise MissingAppConfig("client_id was not provided as an input parameter or in env var 'NanoSSO_client_id'")
            else:
                raise MissingAppConfig("client_id was not provided as an input parameter")
        if not self.secret_key:
            if read_from_env_vars:
                raise MissingAppConfig("secret_key was not provided as an input parameter or in env var 'NanoSSO_secret_key'")
            else:
                raise MissingAppConfig("secret_key was not provided as an input parameter")
        if not self.callback:
            if read_from_env_vars:
                raise MissingAppConfig("callback was not provided as an input parameter or in env var 'NanoSSO_callback'")
            else:
                raise MissingAppConfig("callback was not provided as an input parameter")
