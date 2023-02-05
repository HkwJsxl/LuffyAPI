# 开发阶段配置文件

import os
import sys
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# settings配置文件移动后要将这个settings添加到环境变量中
sys.path.insert(0, BASE_DIR)
# 将所有app目录的根加入到环境变量中，后续无需更改app的引入方式
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = "django-insecure-6#)3o)!19s5=4aequ3_hl$r73y0-q_#-jq$eqqk32x=p)e1o2-"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',
    'corsheaders',

    'user.apps.UserConfig',
    'home.apps.HomeConfig',
    'course.apps.CourseConfig',
    'order.apps.OrderConfig'

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "LuffyAPI.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LuffyAPI.wsgi.application"

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffyapi',
        'USER': 'luffyapi',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/shanghai"

USE_I18N = True

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)
AUTH_USER_MODEL = 'user.userinfo'

# 日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            # 实际开发建议使用WARNING
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            # 实际开发建议使用ERROR
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名,日志保存目录必须手动创建
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs", "luffy.log"),
            # 日志文件的最大值,300M
            'maxBytes': 300 * 1024 * 1024,
            # 日志文件的数量,设置最大日志数量为10
            'backupCount': 100,
            # 日志格式:详细格式
            'formatter': 'verbose',
            # 文件内容编码
            'encoding': 'utf-8'
        },
    },
    # 日志对象
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

# redis缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "PASSWORD": os.getenv('REDIS_PASSWORD'),
        }
    }
}

REST_FRAMEWORK = {
    # 异常处理
    # 'EXCEPTION_HANDLER': 'LuffyAPI.extension.exceptions.re_exception_handler',
    # 分页配置(?limit=1,符合筛选条件的取出一条)
    "DEFAULT_PAGINATION_CLASS": "LuffyAPI.extension.page.ReLimitOffsetPagination",
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    # 额外允许的请求头
    'token',
]

# 腾讯发送验证码
TX_SMS_ID = 'AKIDxjGakeIfmeFamiO1PedMq56rNfqqbIly'
TX_SMS_KEY = os.getenv('TX_SMS_KEY')
TX_SMS_TEMPLATE_ID = "1675402"
TX_SMS_SDK_APP_ID = "1400792152"
TX_SMS_SIGN_NAME = "hkwJsxl公众号"
# 验证码缓存格式(手机号占位符)
TX_SMS_CODE = 'TX_SMS_CODE_%s'
# 过期时间（整数）
TX_SMS_CODE_EXPIRATION = '3'

# 缓存
# 首页轮播图
HOME_BANNER_LIST = ''
HOME_BANNER_EXPIRATION = 60 * 60 * 24

# 首页轮播图返回条数
HOME_BANNER_COUNT = 4

# 路径和端口号
BACKEND_URL = 'http://127.0.0.1:8000'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = '3306'
# 前台基URL
FRONT_END_URL = 'http://127.0.0.1:8080'

# 阿里支付
ALI_SERVER_URL = 'https://openapi.alipaydev.com/gateway.do'
ALI_APP_ID = '2021000122613847'
ALI_APP_PRIVATE_KEY = 'MIIEpAIBAAKCAQEAk5pvzwJUdZI1R3r9qf4Eo5XD6ixe53tId4ERr2axZbmjWsVlv1nMY5kQcBxa3MVWMC6ps3FPiHlSIOwplstgEZrN4YYIPIzrL8ln6FlTHzSR14RLJnjcjsG+nIZHrUjBzm1VZWXDq4aqZrHp/2qTbTJ/T261cZkAUCyzUEPt4jfFVAfNEJS8DjUlaAN6Ho+LBbo/znhJ46zyxg1lkTOf9xcaIne9rWYEuSCJQ/3dmbrV9o4iVdHN2QOmMpq/00KVUm3vC2u8kYYj1sDuN3uDIUPjP+rDd9iu9Az5DcHInNm6CohxDa/sdfQhB/TKzdREVxZV43uzuzaPzgp/47OHgQIDAQABAoIBAEUlKs2R7Njq9jSXJC+3RJsRdKbFxGuyMB9zgkJl3CKoVSMXp/N88KeTs8ShM9uKQjbuFSdvpG9tThEIMO9oNIfquhm0/TTIWwCW3CtXdP4AVXXdjormQYRKtK2Eph1CITA/vapzgrderYLQQ6sYVRnpdwRR+4PMxf3JAvNN7ylyejOoj81XSvEUsURq55/bDApQ9YrjqJwdkdCsWkmVVUDVxX5h0qUO4fHHmHPo6bXyqjWKzF8TTvgk9EuDl15BIObB1lN8UbkEe/Z5cjJn7x/FeOhLkbceyoNz5t/cYDaM6W28EJsEGo1QNxFMUCiEb2/bG+DwHFAy247WrR+pOXECgYEA0pcHx4gs5QlW/UH+2cmExeVhBx42tWZv1scz/pUBP4WikexExA7JQT4QqtSmcoSCKH3SqtDG7pXlbZhg/umMs+auNWt4hZTCQMio1tVAR65QWtFzo6NcmdEQW7GaA2AU+zSn09ejccBkdvBFto0hKK2OW9PuAxAjtGFqxM+jJ00CgYEAs25rjQrebXV9kbZ/ZuHKShJ9bafmOkssRCSwGiE7Lvx3ShSRPdIyvVrQAsLyzymhggBXUoO4JUSz9+iVVhCWtcDP4mfaBcENMNY7LJKzsaht7ZAKW2LX8UMvwqBtx6GSTlxKLTMTB1WakWgDhOpdxbcI81CEzJdeTkogKzpvTwUCgYEAh94vg7nFFWRoPm/U6FiPFEsAxeHldDYKFC1jy24BZyVmFPW2DDRp/nD3ufAHD72UaGF9iP24S3hklMgKVI0EXZGIdijHko++oKOV4z2lAlpht6aJEFu2w/rRrgcxEdpszwJTAWeQKTTy3JX6tGPrr94CChb66fkAwEFV7HL2lcUCgYAoqPYAQR1ESqKI2YUnSDUx8dywc6KtRQmj63hog21I6XcSt3RuQOq0lBac+ZZSMYnizrb7ANRCxb3OiMsGdL3iM+4nzQbP1P5rObCxGhFUSemXMtPV/6EVj/cLsJUP7uIblbhNY8yFFfXvy1U40m8rdZ22nWFqh0ackRmXEifVDQKBgQCKU6c7D3QFsUh6XIkwVdpsmurXUP9zjx6FkojxmR9YBNPS18Qe+VaH4rLB21i91r10ZmN4DIJ+4wdWcYaGxn1QqIjTToAAItmgt+nsmD8ivLpusjOtwl9dBJ/qhsmmQqpAh+xqtkpxI5G+oYm/31OGiQ68UhDqWORVhtDr4FjQmA=='
ALI_ALIPAY_PUBLIC_KEY = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsXIPhjMy0pTyq6vG9Dkva9pzzL7mMPaxY6IXEx89fJulG052qYCCbmB5PrqKefSGJk2N++Am3a0vhyzUURQnQGH4vruCZX1iWuzw3QwlZuuedxFM/uciXUZELe4Vin6qW59thx2slna11FayGbM5jKVmR1g8HJvxECFuMxYIZC5tvaJbsbJbAPYESWkuAh1M1nspJmP3LuqXCLpeLXOYpdhn+6lTtGbArvzuXyrdbZurnqWTb3Q8M9nFZkKwuLKkZCeO8Qs3iy7mSzayNsvwJ8kf/SooOMRIAe9I5lqIbECfV2+VzsfXSXahYvpL1osQTQOgjAT13dZvM9Hfyt6d/wIDAQAB'
ALI_GATEWAY_URL = 'https://openapi.alipaydev.com/gateway.do?'
# 卖家id
ALI_SELLER_ID = '2088621995167585'
# 支付宝同步异步回调接口配置
# 后台异步回调接口
NOTIFY_URL = BACKEND_URL + "/order/pay/success/"
# 前台同步回调接口
RETURN_URL = FRONT_END_URL + "/pay/success"

# jwt token过期时间
TOKEN_EXPIRATION = ''
