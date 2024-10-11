from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Serve static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templating setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the app with uvicorn: uvicorn main:app --reload
