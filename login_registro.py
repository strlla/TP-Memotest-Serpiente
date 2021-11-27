
import csv

def guardar_nuevo_usuario(usuario):    
    with open('usuarios.csv', 'a') as csvfile:
        fieldnames = ['usuario', 'clave']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(usuario)
        csvfile.close()

def obtener_usuarios():
    usuarios = []
    with open('usuarios.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
        for fila in spamreader:
            if fila:
                usuarios.append({"usuario": fila[0], "clave": fila[1] })
    
    return usuarios[1:len(usuarios)]        
    

def iniciar_sesion(usuario, contrasenia, mostrar_mensaje):
    usuarios = obtener_usuarios()
    if not usuario or not contrasenia:
        mostrar_mensaje("Por favor, complete los dos campos", False)
        return
    usuarioEncontrado = next((x for x in usuarios if x["usuario"] == usuario), None)
    if not usuarioEncontrado: 
        mostrar_mensaje("No esta registrado", False)
    elif (usuarioEncontrado['clave'] == contrasenia):
        print("logueado!") 
        mostrar_mensaje("Usuario logueado!", True)
    else: mostrar_mensaje("Contraseña incorrecta", False)