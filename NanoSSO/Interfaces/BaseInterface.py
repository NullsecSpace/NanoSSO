from NanoSSO import SSO


class BaseInterface:
    def __init__(self, **kwargs):
        self.SSO = SSO(**kwargs)

    def run(self):
        raise NotImplemented
