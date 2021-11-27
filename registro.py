
import csv

class Registro:
    jugadores_logueados = []
    def __init__(self) -> None:
        pass
    
    def agregar_jugador_logueado(self, jugador): 
        self.jugadores_logueados.append(jugador)
        
    def guardar_nuevo_usuario(usuario):    
        with open('usuarios.csv', 'a') as csvfile:
            fieldnames = ['usuario', 'clave']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(usuario)
            csvfile.close()

    def obtener_usuarios(self):
        usuarios = []
        with open('usuarios.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
            for fila in spamreader:
                if fila:
                    usuarios.append({"usuario": fila[0], "clave": fila[1] })
            
        return usuarios[1:len(usuarios)]        
    
    def iniciar_sesion(self, usuario, contrasenia, mostrar_mensaje):
        usuarios = self.obtener_usuarios()
        if not usuario or not contrasenia:
            mostrar_mensaje("Por favor, complete los dos campos", False)
            return
        usuarioEncontrado = next((x for x in usuarios if x["usuario"] == usuario), None)
        if not usuarioEncontrado: 
            mostrar_mensaje("No está registrado", False)
        elif (usuarioEncontrado['clave'] == contrasenia):
            usuarioLogueado = next((x for x in Registro.jugadores_logueados if x["usuario"] == usuario), None)
            if usuarioLogueado:
                mostrar_mensaje("Ya está logueado", False)
            else:                 
                mostrar_mensaje("Se logueo correctamente", True)
                self.agregar_jugador_logueado(usuarioEncontrado)
            print(Registro.jugadores_logueados)
        else: mostrar_mensaje("Contraseña incorrecta", False)