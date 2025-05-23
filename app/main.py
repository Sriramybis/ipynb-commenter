from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import shutil
import os
import uuid
from auto_comment import process_notebook

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_notebook(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    uid = uuid.uuid4().hex
    input_path = f"uploaded_{uid}.ipynb"
    output_path = f"processed_{uid}.ipynb"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_notebook(input_path, output_path)

    # Schedule the temp files to be deleted after response
    background_tasks.add_task(os.remove, input_path)
    background_tasks.add_task(os.remove, output_path)

    return FileResponse(
        path=output_path,
        filename="auto_commented_notebook.ipynb",
        media_type='application/json',
        background=background_tasks
    )