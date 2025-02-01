# creates a worker to monitor and execute the tasks.
from app.tasks import celery_app

if __name__ == '__main__':
    celery_app.worker_main()
