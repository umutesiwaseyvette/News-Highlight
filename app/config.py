class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_API_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True