from random import sample
from conexionBD import *  # Importando conexión BD


def listaProductos():
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM productos ORDER BY id DESC"
    cur.execute(querySQL)
    resultadoBusqueda = cur.fetchall()
    totalBusqueda = len(resultadoBusqueda)

    cur.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda


def updateProducto(id=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos WHERE id = %s LIMIT 1", [id])
    resultQueryData = cursor.fetchone()
    return resultQueryData


def registrarProducto(nombre='', memo='', nuevoNombreFile='', enlacesGaleria='', fecha_publicacion='', categoria=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    sql = "INSERT INTO productos(nombre, imagen, memo, galeria, fecha_publicacion, categoria) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nombre, memo, nuevoNombreFile, enlacesGaleria, fecha_publicacion, categoria)

    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    resultado_insert = cursor.rowcount
    ultimo_id = cursor.lastrowid

    cursor.close()
    conexion_MySQLdb.close()

    return resultado_insert


def detallesdelProducto(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos WHERE id ='%s'" % (id))
    resultadoQuery = cursor.fetchone()

    cursor.close()
    conexion_MySQLdb.close()

    return resultadoQuery


def recibeActualizarProducto(nombre, memo, nuevoNombreFile, enlacesGaleria, fecha_publicacion, categoria, id):
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)

    try:
        cur.execute("""
            UPDATE productos
            SET 
                nombre   = %s,
                memo    = %s,
                imagen  = %s,
                galeria = %s,
                fecha_publicacion = %s,
                categoria = %s
            WHERE id=%s
        """, (nombre, memo, nuevoNombreFile, enlacesGaleria, fecha_publicacion, categoria, id))

        conexion_MySQLdb.commit()
        resultado_update = cur.rowcount
    except Exception as e:
        print(f"Error updating product: {e}")
        conexion_MySQLdb.rollback()
        resultado_update = 0
    finally:
        cur.close()
        conexion_MySQLdb.close()

    return resultado_update


def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud = 20
    secuencia = string_aleatorio.upper()
    resultado_aleatorio = sample(secuencia, longitud)
    string_aleatorio = "".join(resultado_aleatorio)
    return string_aleatorio


if __name__ == "__main__":
    # Agrega aquí la parte del código para ejecutar la aplicación Flask si es necesario.
    pass
