# fix for mac machines
import os
from _scproxy import _get_proxy_settings

_get_proxy_settings()
os.environ["NO_PROXY"] = "*"
