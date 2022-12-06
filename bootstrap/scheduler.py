import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from app.jobs.demo_job import demo_job
from app.providers import logging_provider


def create_scheduler() -> BlockingScheduler:
    logging_provider.register()

    logging.info("BlockingScheduler initializing")

    scheduler: BlockingScheduler = BlockingScheduler()

    register_job(scheduler)

    return scheduler


def register_job(scheduler):
    """
     注册调度任务
    """
    scheduler.add_job(demo_job, 'interval', seconds=5)
