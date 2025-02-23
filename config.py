from cachelib.file import FileSystemCache
from sqlalchemy.pool import QueuePool
from superset.superset_typing import CacheConfig

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
}

ENABLE_PROXY_FIX = True
SECRET_KEY = "YOUR_OWN_RANDOM_GENERATED_STRING"

ENABLE_CORS = True
CORS_ALLOW_CREDENTIALS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["*"],
}
FAB_ADD_SECURITY_API = True

# Guest configuration for embedding dashboards
GUEST_ROLE_NAME = "Public"
GUEST_TOKEN_JWT_SECRET = "random_string"
GUEST_TOKEN_JWT_EXP_SECONDS = 3600  # 1 hour
AUTH_ROLE_PUBLIC = "Public"

DEFAULT_FEATURE_FLAGS = {
    "DASHBOARD_RBAC": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DYNAMIC_PLUGINS": True,
    "OPTIMIZE_SQL": True,
    "ESTIMATE_QUERY_COST": True,
}

THUMBNAIL_CACHE_CONFIG: CacheConfig = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_NO_NULL_WARNING": True,
}

CACHE_CONFIG: CacheConfig = {"CACHE_TYPE": "SimpleCache"}
DATA_CACHE_CONFIG: CacheConfig = {"CACHE_TYPE": "SimpleCache"}
EXPLORE_FORM_DATA_CACHE_CONFIG: CacheConfig = {"CACHE_TYPE": "SimpleCache"}

SESSION_SERVER_SIDE = True
SESSION_TYPE = "cachelib"
SESSION_CACHELIB = FileSystemCache(cache_dir="/tmp/flask_session", threshold=500)
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
WTF_CSRF_ENABLED = True

TALISMAN_ENABLED = False
OVERRIDE_HTTP_HEADERS = {"X-Frame-Options": "ALLOWALL"}
HTTP_HEADERS = {"X-Frame-Options":"ALLOWALL"}

SQLALCHEMY_ENGINE_OPTIONS = {
    'poolclass': QueuePool,
    'pool_pre_ping': True,
    'pool_size': 30,
    'max_overflow': 10,
    'pool_timeout': 120,
    'pool_recycle': 1800,
}
