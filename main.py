from fastapi import FastAPI
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoApp.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

app = FastAPI()

from todos.models import Todo
@app.get("/")
async def root():
    return list(Todo.objects.all().order_by('-created_at').values())