from os import environ as env

CURRENT_CHANNEL = "invoice"
NEXT_CHANNEL = "notify"
NOTIFY_CHANNEL = "notify"

SUBSCRIPTION_TIMEOUT = 10    # in seconds

# redis
REDIS_HOST = env.get("REDIS_HOST", "localhost")
REDIS_PORT = int(env.get("REDIS_PORT", "6379"))
REDIS_USERNAME = env.get("REDIS_USERNAME")
REDIS_PASSWORD = env.get("REDIS_PASSWORD")
