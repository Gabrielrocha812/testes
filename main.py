from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
app = FastAPI()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/testes")
async def home(request: Request):
    return templates.TemplateResponse("teste.html", {"request": request})

