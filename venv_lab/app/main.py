from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/ping", status_code=307)


@app.get("/ping")
async def ping():
    return {"status": "ok"}


