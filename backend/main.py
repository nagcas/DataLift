from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def dataLift():
    return 'Benvenuti su DataLift'

