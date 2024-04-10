# Importaciones de la biblioteca estándar
import json
from flask import Flask, request, jsonify, make_response

# Importaciones de terceros
from Modelo.Platillo import Platillo
from Modelo.Gato import Gato
from Modelo.Solicitud import Solicitud
from Modelo.Usuario import usuario as User

# Importaciones locales
from Controller.PlatilloController import PlatilloController
from Controller.GatoController import GatoController
from Controller.SolicitudController import SolicitudController
from Controller.UsuarioController import UsuarioController


app = Flask(__name__, static_url_path="")

port = 5000


# Función para añadir los encabezados CORS a las respuestas
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


app.after_request(after_request)


@app.route("/endp1", methods=["POST"])
def endp_func1():
    return jsonify({"message": "Endpoint 1: Porsche Carrera"})


@app.route("/endp2", methods=["POST"])
def endp_func2():
    return jsonify({"message": "Endpoint 2: Porsche Turbo S"})


@app.route("/endp3", methods=["POST"])
def endp_func3():
    return jsonify({"message": "Endpoint 3: Porsche GT3"})


# User//////////////////////////////////////////////////////////////////////
@app.route("/user/validar", methods=["POST"])
@app.route("/user/crear", methods=["POST"])
def handle_user_request():
    data = request.get_json()
    if not data or "usuario" not in data or "contraseña" not in data:
        return jsonify({"error": "Datos insuficientes"}), 400

    us = User(data["usuario"], data["contraseña"])

    if request.url_rule.rule == "/user/validar":
        return jsonify(UsuarioController().validarUser(us))
    elif request.url_rule.rule == "/user/crear":
        return jsonify(UsuarioController().crearUsuario(us))


# Platillo//////////////////////////////////////////////////////////////////
def crear_platillo_desde_data(data):
    if (
        not data
        or "nombre" not in data
        or "descripcion" not in data
        or "foto" not in data
    ):
        return None, {"error": "Datos insuficientes"}
    return (
        Platillo(
            nombre=data["nombre"], descripcion=data["descripcion"], foto=data["foto"]
        ),
        None,
    )


@app.route("/platillo/listar", methods=["POST"])
def listar_platillos():
    return jsonify(PlatilloController().listar())


@app.route("/platillo/guardar", methods=["POST"])
def guardar_platillo():
    data = request.get_json()
    platillo, error = crear_platillo_desde_data(data)
    if error:
        return jsonify(error), 400
    return jsonify(PlatilloController().guardar(platillo))


@app.route("/platillo/modificar", methods=["POST"])
def modificar_platillo():
    data = request.get_json()
    if (
        not data
        or "id" not in data
        or "nombre" not in data
        or "descripcion" not in data
        or "foto" not in data
    ):
        return jsonify({"error": "Datos insuficientes"}), 400
    platillo = Platillo(
        id=data["id"],
        nombre=data.get("nombre"),
        descripcion=data.get("descripcion"),
        foto=data.get("foto"),
    )
    return jsonify(PlatilloController().modificar(platillo))


@app.route("/platillo/eliminar", methods=["POST"])
def eliminar_platillo():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Datos insuficientes"}), 400
    platillo = Platillo(id=data["id"])
    return jsonify(PlatilloController().eliminar(platillo))


# Gato//////////////////////////////////////////////////////////////////////
def crear_gato_desde_data(data):
    if (
        not data
        or "nombre" not in data
        or "sexo" not in data
        or "disponibilidad" not in data
        or "edad" not in data
        or "foto" not in data
    ):
        return None, {"error": "Datos insuficientes"}
    return (
        Gato(
            nombre=data["nombre"],
            sexo=data["sexo"],
            disponibilidad=data["disponibilidad"],
            edad=data["edad"],
            foto=data["foto"],
        ),
        None,
    )


@app.route("/gato/listar", methods=["GET"])
def listar_gatos():
    return jsonify(GatoController().listar())


@app.route("/gato/registrar", methods=["POST"])
def registrar_gato():
    data = request.get_json()
    gato, error = crear_gato_desde_data(data)
    if error:
        return jsonify(error), 400
    return jsonify(GatoController().registrar(gato))


@app.route("/gato/modificar", methods=["POST"])
def modificar_gato():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Datos insuficientes"}), 400
    gato = Gato(
        id=data["id"],
        nombre=data.get("nombre"),
        sexo=data.get("sexo"),
        disponibilidad=data.get("disponibilidad"),
        edad=data.get("edad"),
        foto=data.get("foto"),
    )
    return jsonify(GatoController().modificar(gato))


@app.route("/gato/eliminar", methods=["POST"])
def eliminar_gato():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Datos insuficientes"}), 400
    gato = Gato(id=data["id"])
    return jsonify(GatoController().eliminar(gato))


# Solicitud/////////////////////////////////////////////////////////////////
def crear_solicitud_desde_data(data):
    if (
        not data
        or "nombre" not in data
        or "correo" not in data
        or "telefono" not in data
        or "ciudad" not in data
    ):
        return None, {"error": "Datos insuficientes"}
    solicitud = Solicitud(
        nombre=data["nombre"],
        correo=data["correo"],
        telefono=data["telefono"],
        ciudad=data["ciudad"],
        gato=data.get("gato"),
    )
    return solicitud, None


@app.route("/solicitud/guardar", methods=["POST"])
def guardar_solicitud():
    data = request.get_json()
    solicitud, error = crear_solicitud_desde_data(data)
    if error:
        return jsonify(error), 400
    return jsonify(SolicitudController().guardar(solicitud))


@app.route("/solicitud/eliminar", methods=["POST"])
def eliminar_solicitud():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Datos insuficientes"}), 400
    solicitud = Solicitud(id=data["id"])
    return jsonify(SolicitudController().eliminar(solicitud))


@app.route("/solicitud/listar", methods=["GET"])
def listar_solicitudes():
    return jsonify(SolicitudController().listar())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=port, debug=True)
