import logging

from bootstrap.scheduler import create_scheduler

scheduler = create_scheduler()

# 这个是用来调度任务的
if __name__ == "__main__":
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Scheduler will shutdown...")
        scheduler.shutdown()
