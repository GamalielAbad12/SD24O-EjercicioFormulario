from fastapi import FastAPI, Form, UploadFile, File
import os
from typing import Optional
import uuid


app = FastAPI()


@app.get('/')
def prueba_servidor():
    print("Éxito en servidor")
    respuesta = {"Exito":"El servidor se levantó"}

    return respuesta

@app.post('/fotos')
async def guardar_fotos(nombre:str=Form(...), direccion:str=Form(...), foto:UploadFile=File(...), paseVip:bool=Form(False)):
    print(nombre)
    print(direccion)
    print(paseVip)
    home_usuario = os.path.expanduser("~")
    carpeta_vip = f"{home_usuario}/fotos-usuarios-vip"
    carpeta_no_vip = f"{home_usuario}/fotos-usuarios"

    if paseVip == False:
        carpeta = carpeta_no_vip
    else:
        carpeta = carpeta_vip
    
    os.makedirs(carpeta, exist_ok=True)



    nombre_arcivo = uuid.uuid4()
    extension_foto = os.path.splitext(foto.filename)[1]
    ruta_imagen = f'{carpeta}/fotos_ejemplo{nombre_arcivo}{extension_foto}'
    print("Guardando foto en ", ruta_imagen)
    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read()
        imagen.write(contenido)
    



    respuesta = {
        "Nombre": nombre,
        "direccion": direccion,
        "ruta_imagen": ruta_imagen,
        "paseVip": paseVip
    }
    return respuesta