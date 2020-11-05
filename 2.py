
from threading import Event
import asyncio
import time
import os
import sys
import datetime
from fastapi import FastAPI

now = datetime.datetime.now()
import asyncio

app = FastAPI()

@app.get("/1")
async def root():
    return {
str(open('sample.txt', 'r').read())}
file_object = open('sample.txt', 'a' ,newline='\n')
file_object.write(' Hello 2 ! \r \n')
file_object.write(str(now))
file_object.close()
# Python 3.7+