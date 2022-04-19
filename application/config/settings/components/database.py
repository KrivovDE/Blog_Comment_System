import environ

env = environ.Env()
DATABASES = {"default": env.db("DATABASE_URL", 'postgres://debug:debug@127.0.0.1:5432/krivov')}
