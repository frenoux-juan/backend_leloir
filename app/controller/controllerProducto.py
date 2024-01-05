from random import sample
from conexionBD import *  #Importando conexion BD



#Creando una funcion para obtener la lista de productos.
def listaProductos():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM productos ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateProducto(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarProducto(nombre='', memo='', nuevoNombreFile='', enlacesGaleria=''):
    # Establecer la conexión a la base de datos MySQL
    conexion_MySQLdb = connectionBD()
    
    # Crear un objeto cursor para ejecutar consultas SQL
    cursor = conexion_MySQLdb.cursor(dictionary=True)
        
    # Definir la consulta SQL para la inserción de un nuevo producto
    sql = ("INSERT INTO productos(nombre, imagen, memo, galeria) VALUES (%s, %s, %s, %s)")
    
    # Especificar los valores a insertar en la consulta SQL
    valores = (nombre, memo, nuevoNombreFile, enlacesGaleria)
    
    # Ejecutar la consulta SQL con los valores proporcionados
    cursor.execute(sql, valores)
    
    # Confirmar los cambios en la base de datos
    conexion_MySQLdb.commit()
    
    # Obtener el número de filas afectadas por la inserción
    resultado_insert = cursor.rowcount
    
    # Obtener el ID del último registro insertado
    ultimo_id = cursor.lastrowid
    
    # Cerrar el cursor para liberar recursos
    cursor.close()
    
    # Cerrar la conexión a la base de datos
    conexion_MySQLdb.close()
    
    # Devolver el número de filas afectadas por la inserción
    return resultado_insert

  

def detallesdelProducto(id):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM productos WHERE id ='%s'" % (id))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    


def recibeActualizarProducto(nombre, memo, nuevoNombreFile, enlacesGaleria, id):
    conexion_MySQLdb = connectionBD()
    cur = conexion_MySQLdb.cursor(dictionary=True)

    try:
        # Actualizar producto con imagen y galería
        cur.execute("""
            UPDATE productos
            SET 
                nombre   = %s,
                memo    = %s,
                imagen  = %s,
                galeria = %s
            WHERE id=%s
        """, (nombre, memo, nuevoNombreFile, enlacesGaleria, id))

        conexion_MySQLdb.commit()
        resultado_update = cur.rowcount  # Retorna 1 o 0
    except Exception as e:
        print(f"Error updating product: {e}")
        conexion_MySQLdb.rollback()
        resultado_update = 0
    finally:
        cur.close()
        conexion_MySQLdb.close()

    return resultado_update
 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio