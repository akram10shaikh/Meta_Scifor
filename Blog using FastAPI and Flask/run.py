import uvicorn
from back.main import app as fastapi_app
from multiprocessing import Process
import os

def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    p = Process(target=run_fastapi)
    p.start()
    os.system("python manage.py runserver 127.0.0.1:800")