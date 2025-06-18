def bucle1():
    while True:
        mypass = input('Ingrese una contrasenha: \n')
        confirm = input('Confirme su contrasenha: \n' )
    
        if mypass == confirm:
            print("Contrasenha confirmada correctamente.")
            
            # Solo si confirma correctamente, se activa el login:
            while True:
                respuesta = input('Inicia sesion: \n')
                if respuesta == mypass:
                    print('Login exitoso')
                    return
                else: 
                    print('Contrasenha incorrecta') 
        else: 
            print('Confirmacion erronea, ingrese nuevamente')
            
bucle1()


