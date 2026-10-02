import json
import os

from django.shortcuts import render, redirect


def login(request):

    error = ""

    if request.method == "POST":

        usuario = request.POST.get("usuario")
        password = request.POST.get("password")

        ruta = os.path.join(
            os.path.dirname(__file__),
            "datos",
            "usuarios.json"
        )

        with open(ruta, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)

        for dato in usuarios:

            if dato["usuario"] == usuario and dato["password"] == password:
                return redirect("inicio")

        error = "Usuario o contraseña incorrectos"

    return render(request, "login.html", {"error": error})


def inicio(request):
    return render(request, "inicio.html")

def registrar(request):

    mensaje = ""

    if request.method == "POST":

        ruta = os.path.join(
            os.path.dirname(__file__),
            "datos",
            "mascotas.json"
        )

        with open(ruta, "r", encoding="utf-8") as archivo:
            mascotas = json.load(archivo)

        nueva_mascota = {
            "id": len(mascotas) + 1,
            "dueno": request.POST.get("dueno"),
            "telefono": request.POST.get("telefono"),
            "mascota": request.POST.get("mascota"),
            "tipo": request.POST.get("tipo"),
            "raza": request.POST.get("raza"),
            "edad": request.POST.get("edad"),
            "sexo": request.POST.get("sexo"),
            "motivo": request.POST.get("motivo")
        }

        mascotas.append(nueva_mascota)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(mascotas, archivo, indent=4, ensure_ascii=False)

        mensaje = "Mascota registrada correctamente"

    return render(request, "registrar.html", {"mensaje": mensaje})

def consultar(request):

    ruta = os.path.join(
        os.path.dirname(__file__),
        "datos",
        "mascotas.json"
    )

    with open(ruta, "r", encoding="utf-8") as archivo:
        mascotas = json.load(archivo)

    return render(request, "consultar.html", {"mascotas": mascotas})

def editar(request, id):

    ruta = os.path.join(
        os.path.dirname(__file__),
        "datos",
        "mascotas.json"
    )

    with open(ruta, "r", encoding="utf-8") as archivo:
        mascotas = json.load(archivo)

    mascota_encontrada = None

    for mascota in mascotas:
        if mascota["id"] == id:
            mascota_encontrada = mascota
            break

    if request.method == "POST":

        mascota_encontrada["dueno"] = request.POST.get("dueno")
        mascota_encontrada["telefono"] = request.POST.get("telefono")
        mascota_encontrada["mascota"] = request.POST.get("mascota")
        mascota_encontrada["tipo"] = request.POST.get("tipo")
        mascota_encontrada["raza"] = request.POST.get("raza")
        mascota_encontrada["edad"] = request.POST.get("edad")
        mascota_encontrada["sexo"] = request.POST.get("sexo")
        mascota_encontrada["motivo"] = request.POST.get("motivo")

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(mascotas, archivo, indent=4, ensure_ascii=False)

        return redirect("consultar")

    return render(
        request,
        "editar.html",
        {"mascota": mascota_encontrada}
    )