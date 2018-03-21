from celery import shared_task

from mysite.celery import app


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def tutorial_add(x, y):
    print("Adding %d and %d" % (x, y))
    return x + y


@shared_task
def tutorial_shared_task():
    print("This is a shared_task creatd")
