from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
IP = env.str('IP')
BOT_USERNAME = env.str('BOT_USERNAME')

POSTGRES_USER = env.str('SQL_USER')
POSTGRES_PASSWORD = env.str('SQL_PASSWORD')
POSTGRES_SERVER = env.str('SQL_SERVER')
POSTGRES_PORT = env.str('SQL_PORT')
POSTGRES_DB = env.str('SQL_DB')

POSTGRESQL_URL = f'{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}'
DATABASE_URL = "postgresql+psycopg2://" + POSTGRESQL_URL
