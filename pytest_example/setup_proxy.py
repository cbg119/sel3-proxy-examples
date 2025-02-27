import os
import urllib3
import pytest

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
        urllib3.PoolManager = lambda *args, **kwargs: urllib3.ProxyManager(proxy_url, *args, **kwargs)