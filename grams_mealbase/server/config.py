import os

class BaseConfig:
    """Base configuration with defaults shared across all environments."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'mealbase_session'

    # Default database (can be overridden)
    DB_PATH = os.path.join(os.path.dirname(__file__), 'food.db')  
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    DATABASE_URI = SQLALCHEMY_DATABASE_URI

    # Other common settings can go here
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    # Optional: different DB for dev
    DB_PATH = os.path.join(os.path.dirname(__file__), 'dev_food.db')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    DATABASE_URI = SQLALCHEMY_DATABASE_URI


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    # Use in-memory database for speed
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(BaseConfig):
    """Production configuration."""
    # Override with a real production database URL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///prod.db')
    DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = False
    TESTING = False