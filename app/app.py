from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from controller.controllerProducto import *
import json


from flask_cors import CORS #HABILITA QUE PARA QUE EL BACKEND SE PUEDA CONSUMIR DESDE OTRO SERVIDOR
#ANTES LO TENGO QUE INSTALAR EN LA CONSOLA pip install flask-cors



#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

# Configurando la clave secreta para sesiones
app.secret_key = '19562436554'

CORS(app) #HABILITA QUE PARA QUE EL BACKEND SE PUEDA CONSUMIR DESDE OTRO SERVIDOR

msg  =''
tipo =''




# Lista de usuarios y contraseñas (reemplaza con tus usuarios reales)
usuarios = {
    'Admin': 'Leloir2014ok',
    'usuario2': 'contraseña2',
    'usuario3': 'contraseña3'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario_ingresado = request.form.get('username')
        contraseña_ingresada = request.form.get('password')

        if usuario_ingresado in usuarios and contraseña_ingresada == usuarios[usuario_ingresado]:
            session['logged_in'] = True
            session['username'] = usuario_ingresado
            return redirect(url_for('inicio'))
        else:
            return render_template('/public/login.html', error='Credenciales incorrectas')
    return render_template('/public/login.html')


@app.route('/layout')
def inicio():
    if 'logged_in' in session and session['logged_in']:
        return render_template('/public/layout.html', miData=listaProductos())
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


#RUTAS
@app.route('/registrar-producto', methods=['GET','POST'])
def addProducto():
    return render_template('public/acciones/add.html')


 
# Registrando nuevo producto
@app.route('/producto', methods=['POST'])
def formAddProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        memo = request.form['memo']
        fecha_publicacion = request.form['fecha_publicacion']
        categoria = request.form['categoria']

        # Verificar que se haya cargado un archivo
        if 'imagen' in request.files and request.files['imagen'].filename != '':
            file = request.files['imagen']
            nuevoNombreFile = recibeFoto(file)

            # Obtener el enlace de la galería desde el formulario (lista de archivos si se seleccionan múltiples)
            enlacesGaleria = request.files.getlist('enlace_galeria[]')

            # Procesar cada imagen de la galería
            galeria = []
            for file in enlacesGaleria:
                nuevoNombreFileGaleria = recibeFoto(file)
                galeria.append(nuevoNombreFileGaleria)

            # Convertir la lista de enlaces de la galería a una cadena JSON
            galeria_json = json.dumps(galeria)

            # Llamada a la función registrarProducto con los nuevos campos "fecha_publicacion" y "categoria"
            resultData = registrarProducto(fecha_publicacion, nombre, nuevoNombreFile, memo, galeria_json, categoria)

            # Verificar el resultado de la operación
            if resultData == 1:
                return render_template('public/layout.html', miData=listaProductos(), msg='El Registro fue un éxito', tipo=1)
            else:
                return render_template('public/layout.html', msg='Error al registrar el producto', tipo=1)
        else:
            return render_template('public/layout.html', msg='Debe cargar una foto', tipo=1)

@app.route('/form-update-producto/<string:id>', methods=['GET', 'POST'])
def formViewUpdate(id):
    if request.method == 'GET':
        resultData = updateProducto(id)
        if resultData:
            return render_template('public/acciones/update.html', dataInfo=resultData)
        else:
            return render_template('public/layout.html', miData=listaProductos(), msg='No existe el producto', tipo=1)
    else:
        return render_template('public/layout.html', miData=listaProductos(), msg='Metodo HTTP incorrecto', tipo=1)
   
  
@app.route('/ver-detalles-del-producto/<int:id>', methods=['GET', 'POST'])
def viewDetalleProducto(id):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelProducto(id) #Funcion que almacena los detalles del producto
        
        if resultData:
            return render_template('public/acciones/view.html', infoProducto = resultData, msg='Detalles del Producto', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el Producto', tipo=1)
    return redirect(url_for('inicio'))
    

# Nueva función para actualizar un producto
def actualizarProducto(id, fecha_publicacion, nombre, nueva_imagen, memo, enlaces_galeria_json, categoria):
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)

    # Obtener las imágenes de la galería actuales del producto
    cur.execute('SELECT galeria FROM productos WHERE id=%s', (id,))
    producto_actual = cur.fetchone()
    galeria_actual = json.loads(producto_actual['galeria']) if producto_actual and 'galeria' in producto_actual else []

    # Eliminar las imágenes de la galería existentes si hay alguna
    basepath = os.path.dirname(__file__)
    for imagen in galeria_actual:
        try:
            imagen_path = os.path.join(basepath, 'static/assets/fotos_productos', imagen)
            os.remove(imagen_path)
        except FileNotFoundError:
            # Manejar la excepción si la imagen no se encuentra (no mostrar un error)
            pass

    # Agregar las nuevas imágenes de la galería
    nuevas_imagenes = json.loads(enlaces_galeria_json)

    # Actualizar los campos del producto en la base de datos
    cur.execute('UPDATE productos SET fecha_publicacion=%s, nombre=%s, imagen=%s, memo=%s, galeria=%s, categoria=%s WHERE id=%s',
                (fecha_publicacion, nombre, nueva_imagen, memo, json.dumps(nuevas_imagenes), categoria, id))
    conexion_MySQLdb.commit()

    # Verificar el número de filas afectadas para determinar si la actualización fue exitosa
    resultado_actualizar = cur.rowcount

    return resultado_actualizar

@app.route('/actualizar-producto/<string:id>', methods=['POST'])
def formActualizarProducto(id):
    if request.method == 'POST':
        # Acceder a los datos del formulario usando request.form
        nombre = request.form['nombre']
        memo = request.form['memo']
        fecha_publicacion = request.form['fecha_publicacion']
        categoria = request.form['categoria']
        
        # Manejo de la imagen principal
        nueva_imagen = None
        if 'imagen' in request.files and request.files['imagen']:
            file = request.files['imagen']
            nueva_imagen = recibeFoto(file)

        # Obtener el enlace de la galería desde el formulario (lista de archivos si se seleccionan múltiples)
        enlacesGaleria = request.files.getlist('enlace_galeria[]')

        # Convertir la lista de enlaces de la galería a una cadena JSON
        enlaces_galeria_json = json.dumps([stringAleatorio() + os.path.splitext(file.filename)[1] for file in enlacesGaleria])

        # Actualizar producto con la nueva información
        resultData = actualizarProducto(id, fecha_publicacion, nombre, nueva_imagen, memo, enlaces_galeria_json, categoria)


        # Manejo de resultados
        if resultData:
            return render_template('public/layout.html', miData=listaProductos(), msg='Datos del producto actualizados', tipo=1)
        else:
            return render_template('public/layout.html', miData=listaProductos(), msg='No se pudo actualizar el registro', tipo=1)

    # Código después de return, no se ejecutará
    return render_template('public/layout.html', miData=listaProductos(), msg='Petición no válida', tipo=1)




@app.route('/borrar-producto', methods=['POST'])
def formViewBorrarProducto():
    if request.method == 'POST':
        id = request.form['id']
        imagen = request.form['nombreFoto']
        resultData = eliminarProducto(id, imagen)

        if resultData == 1:
            return jsonify([1])
        else:
            return jsonify([0])

def eliminarProducto(id=''):
    # Establecer la conexión a la base de datos
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)

    # Obtener la información del producto antes de eliminarlo
    cur.execute('SELECT * FROM productos WHERE id=%s', (id,))
    producto = cur.fetchone()

    if not producto:
        return 0  # No existe el producto, retorno indicando que no se realizó la eliminación

    # Obtener las imágenes del producto
    imagen_principal = producto.get('imagen', '')
    galeria_imagen = producto.get('galeria', [])

    # Eliminar el producto de la base de datos
    cur.execute('DELETE FROM productos WHERE id=%s', (id,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount

    # Eliminar la imagen principal del producto
    basepath = os.path.dirname(__file__)
    if imagen_principal:
        imagen_principal_path = os.path.join(basepath, 'static/assets/fotos_productos', imagen_principal)
        try:
            os.remove(imagen_principal_path)
        except FileNotFoundError:
            pass  # No mostrar error si la imagen principal no se encuentra

    # Eliminar las imágenes asociadas a la galería (si existen)
    galeria_path = os.path.join(basepath, 'static/assets/fotos_productos')
    for galeria_imagen_nombre in galeria_imagen:
        galeria_imagen_path = os.path.join(galeria_path, galeria_imagen_nombre)
        try:
            os.remove(galeria_imagen_path)
        except FileNotFoundError:
            pass  # No mostrar error si alguna imagen de la galería no se encuentra

    return resultado_eliminar

def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/assets/fotos_productos', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

       
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    





# Puntos finales de la API algunos no estan funcionales hay que modificarlos, salvo obtener
# todos los productos

# Obtener todos los productos
@app.route('/api/productos', methods=['GET'])
def api_obtener_todos_los_productos():
    productos = listaProductos()
    return jsonify(productos)

# # Obtener detalles de un producto específico
# @app.route('/api/productos/<int:id>', methods=['GET'])
# def api_obtener_detalles_del_producto(id):
#     detalles_producto = detallesdelProducto(id)
#     if detalles_producto:
#         return jsonify(detalles_producto)
#     else:
#         return jsonify({'error': 'producto no encontrado'}), 404

# # Agregar un nuevo producto
# @app.route('/api/productos', methods=['POST'])
# def api_agregar_producto():
#     datos = request.get_json()
#     nombre = datos.get('nombre')
#     memo = datos.get('memo')


#     # Luego, llama a tu función existente para agregar el producto
#     resultado = registrarProducto(nombre, memo, 'sin_foto.jpg')  # Cambia la foto según sea necesario
#     if resultado == 1:
#         return jsonify({'mensaje': 'producto agregado exitosamente'})
#     else:
#         return jsonify({'error': 'No se pudo agregar el producto'}), 400



# # Actualizar detalles de un producto específico
# @app.route('/api/producto/<int:id>', methods=['PUT'])
# def api_actualizar_producto(id_producto):
#     datos = request.get_json()
#     nombre = datos.get('nombre')
#     memo = datos.get('memo')


#     # Luego, llama a tu función existente para actualizar el producto
#     resultado = recibeActualizarProducto(nombre, memo, 'sin_foto.jpg', id)  # Cambia la foto según sea necesario
#     if resultado == 1:
#         return jsonify({'mensaje': 'producto actualizado exitosamente'})
#     else:
#         return jsonify({'error': 'No se pudo actualizar el producto'}), 404



# # Eliminar un producto específico
# @app.route('/api/productos/<int:id>', methods=['DELETE'])
# def api_eliminar_producto(id_producto):
#     # Llamar a tu función existente para eliminar el producto
#     resultado = eliminarProducto(id_producto)
#     if resultado == 1:
#         return jsonify({'mensaje': 'producto eliminado exitosamente'})
#     else:
#         return jsonify({'error': 'No se pudo eliminar el producto'}), 404


# # ... (código existente)



    
if __name__ == "__main__":
    app.run(debug=True, port=8000)