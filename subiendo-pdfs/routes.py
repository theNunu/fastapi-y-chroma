from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile

app = FastAPI(title="subiendo los pdfs")

class Persona(BaseModel):
    name: str
    age:int

    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/guardar/persona")
def save_person(data: Persona):
    data.name
    data.age
    return {
        "message": "se guardo la persona",
        "nombre": data.name,
        "edad": data.age
    }
    

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"nombre del archivo": file.filename,
            "archivo": file,
            "tamaño": file.size
            }
    