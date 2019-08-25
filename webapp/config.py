class Config:
    SECRET_KEY = 'f63f65a3f7274455bfd49edf9c6b36bd'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


config = {
    'default': DevelopmentConfig,
    'testing': TestingConfig
}
