import os

DATABASE_URL: str = os.environ.get('DATABASE_URL') or ''
PGVECTOR_URL: str = os.environ.get('PGVECTOR_URL') or ''

POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST')
POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
DATABASE_PORT: str = os.environ.get('DATABASE_PORT')

MODEL = 'gpt-4o'
