from typing import Optional
import asyncio
from threading import Event
from fastapi import FastAPI, File, UploadFile
from typing import List
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware

import time

app = FastAPI()


import datetime

now = datetime.datetime.now()

origins = [
    "http://localhost",
    "http://localhost:4111",
    "http://localhost:8000",
    "127.0.0.1:59152",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfiles/")
async def create_files(files: bytes = File(...)):
    out_file = open("files/1.jpg", "wb") # open for [w]riting as [b]inary
    out_file.write( bytes([(file) for file in files]))
    out_file.close()


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.get("/1/")
async def root2():
    return {str(open("sample2.txt", "r").read())}


file_object = open("sample2.txt", "a", newline="\n")
file_object.write(" Hello 2 ! \r \n")
file_object.write(str(now))
file_object.close()