class MissingAppConfig(Exception):
    """
    Exception raised when the SSO client cannot be initialized as it does not have client_id, secret_key, or callback defined.
    """