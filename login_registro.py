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
    

def iniciar_sesion(usuario, contrasenia):
    usuarios = obtener_usuarios()
    usuarioEncontrado = next((x for x in usuarios if x["usuario"] == usuario), None)
    if (not usuarioEncontrado): 
        print("el usuario no existe")
    else: 
        if (usuarioEncontrado['clave'] == contrasenia):
            print("logueado!") 