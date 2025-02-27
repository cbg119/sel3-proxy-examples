import os
import urllib3

def get_proxy_url():
    proxy_variables = ["http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY"]
    for proxy_var in proxy_variables:
        if proxy_var in os.environ:
            return os.environ[proxy_var]
proxy_url = get_proxy_url() 

if proxy_url:
    urllib3.PoolManager = lambda *args, **kwargs: urllib3.ProxyManager(proxy_url, *args, **kwargs)