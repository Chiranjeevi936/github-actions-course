
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def main():
    return { "message" : "Hello from github-actions-course!" }


if __name__ == "__main__":
    uvicorn.run("main:app")
