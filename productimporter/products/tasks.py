from celery.decorators import task
from celery.utils.log import get_task_logger
from .utils import load_to_db

logger = get_task_logger(__name__)

@task(name="load_to_db_task")
def load_to_db_task():
    logger.info("started loading")
    return load_to_db()