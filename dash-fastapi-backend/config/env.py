class JwtConfig:
    """
    Jwt配置
    """
    SECRET_KEY = "b01c66dc2c58dc6a0aabfe2144256be36226de378bf87f72c0c795dda67f4d55"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 1440


class DataBaseConfig:
    """
    数据库配置
    """
    HOST = "127.0.0.1"
    PORT = 3306
    USERNAME = 'root'
    PASSWORD = 'mysqlroot'
    DB = 'dash-fastapi'


class RedisConfig:
    """
    Redis配置
    """
    HOST = "127.0.0.1"
    PORT = 6379
    USERNAME = ''
    PASSWORD = ''
    DB = 2