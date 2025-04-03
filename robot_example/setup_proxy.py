import os
import urllib3
from selenium.webdriver.remote.remote_connection import RemoteConnection

def get_proxy_url():
    proxy_variables = ["http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY"]
    for proxy_var in proxy_variables:
        if proxy_var in os.environ:
            return os.environ[proxy_var]
proxy_url = get_proxy_url() 

if proxy_url:
    old_remote_init = RemoteConnection.__init__
    RemoteConnection.__init__ = lambda self, *args, **kwargs: old_remote_init(self, *args, **{**kwargs, 'resolve_ip': False})
    urllib3.PoolManager = lambda *args, **kwargs: urllib3.ProxyManager(proxy_url, *args, **kwargs)