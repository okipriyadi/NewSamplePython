"""
There are a couple of things to note here. First, we are using RabbitMQ as the broker and the backend. Wait, what is the backend? The backend is the resource which returns the results of a completed task from Celery. Second, you may be wondering what amqp is. amqp is a custom protocol that RabbitMQ utilizes
"""

# config file for Celery Daemon

# default RabbitMQ broker
BROKER_URL = 'amqp://'

# default RabbitMQ backend
CELERY_RESULT_BACKEND = 'amqp://'

# specify location of log files
CELERYD_LOG_FILE="celery.log"