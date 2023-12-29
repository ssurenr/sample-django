from mysite.celery import app


@app.task(name="addition")
def add(x, y):
    return x + y
