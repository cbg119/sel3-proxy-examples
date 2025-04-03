import os
import urllib3
import pytest
from selenium.webdriver.remote.remote_connection import RemoteConnection

# This configures the fiture/hook to be ran
# ONCE before every session, to reduce unneccesary calls
@pytest.fixture(scope="session", autouse=True)
def setup_proxy():
    def get_proxy_url():
        proxy_variables = ["http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY"]
        for proxy_var in proxy_variables:
            if proxy_var in os.environ:
                return os.environ[proxy_var]
    proxy_url = get_proxy_url()

    # If a defined proxy environment variable is detected
    # Patches urllib3.PoolManager to create a urllib3.ProxyManager
    # with the specified proxy, and any original arguments
    if proxy_url:
        old_remote_init = RemoteConnection.__init__
        RemoteConnection.__init__ = lambda self, *args, **kwargs: old_remote_init(self, *args, **{**kwargs, 'resolve_ip': False})
        urllib3.PoolManager = lambda *args, **kwargs: urllib3.ProxyManager(proxy_url, *args, **kwargs)