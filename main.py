from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory=Path(__file__).resolve().parent / "mi_trabajo" / "templates")

@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(request=request, name="base.html", context={"request": request})

@app.get("/mascota")
def mascota(request: Request):
    mascota = {
        "nombre": "Drácula",
        "especie": "Mozquito",
        "edad": 2
    }
    return templates.TemplateResponse(request=request, name="mascota.html", context={"request": request, "mascota": mascota})


def get_menu(rol: str):
    if rol == "admin":
        return ["Dashboard", "Usuarios", "Configuración", "Reportes", "Perfil"]
    elif rol == "editor":
        return ["Editar contenido", "Publicaciones", "Perfil"]
    elif rol == "usuario":
        return ["ver contenido"]


@app.get("/acceso")
def acceso_general(request: Request):
    rol = "admin"
    return templates.TemplateResponse(
        request=request,
        name="acceso.html",
        context={"request": request, "rol": rol, "menu": get_menu(rol)},
    )


@app.get("/acceso/{rol}")
def acceso(request: Request, rol: str):
    return templates.TemplateResponse(
        request=request,
        name="acceso.html",
        context={"request": request, "rol": rol, "menu": get_menu(rol)},
    )


@app.get("/recetas")
def recetas(request: Request):
    lista_recetas = [
        {"nombre": "Arroz con pollo", "dificultad": "fácil", "tiempo": 30},
        {"nombre": "Lasaña", "dificultad": "media", "tiempo": 60},
        {"nombre": "Soufflé", "dificultad": "difícil", "tiempo": 90},
        {"nombre": "Ensalada César", "dificultad": "fácil", "tiempo": 15},
    ]
    return templates.TemplateResponse(request=request, name="recetas.html", context={"request": request, "recetas": lista_recetas})