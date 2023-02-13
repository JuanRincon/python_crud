import sys        # Importa librería para su uso en sys.exit()

clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')  # El \ antes de ' permite ingresarlo  sin cerrar el comentario


def list_clients():
    global clients

    print(clients)
    

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:                        # in se encarga de validar que el contenido de la variable client_name esté incluido en el contenido de la variable clients
        clients = clients.replace(client_name + ',', updated_client_name + ',')     # replace es un método para remplazar el contenido de la variable que lo antepone al punto, primero se coloca el valor a reemplazar seguido por el contenido que lo reemplaza
    else:
        print('Client is not in clients list')
        

def delete_client(client_name):
    global clients

    if client_name in clients:
       clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not in clients list')
        

def search_client(client_name):
    clients_list = clients.split(',')     # El método split es para dividir el contenido que tienen la variabla entre contenidos más pequeños cada que se encuentre el valor que se le especifica en este caso la coma

    for client in clients_list:     # client es una variable que se crea acá para ejecutar el ciclo for
        if client != client_name:   
            continue                # continue sirve para salir anticipadamente del ciclo, e indica que no ejecute nada más dentro del bloque del for loop y vete a la siguiente iteración, a diferencia del break que lo que dice es salir completamente de la iteración
        else:
            return True


def _add_comma():
    global clients

    clients += ","


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[L]oad client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]erch client')


def _get_client_name():
    client_name = None     # None deja vacia la variable

    while not client_name:    # while not  dice que mientras no haya la variable ingresela
        client_name = input('What is the client name? ')

        if client_name == 'exit':        # si ingresan exit en el lugar del nombre del cliente (variable) salir
            client_name = None           # se ingresa nuevamente el None para borrar el exit de la variable antes de salir
            break                        # el break sirve para salir del loop while, a diferencia del continue que se explicó más arriba

    if not client_name:                  # este condicional sirve para dejar de ejecutar el programa
            sys.exit()

    return client_name                   # este return permite que la función regrese o devuelva el nombre del cliente que es la variable


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name() 
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name() 
        updated_client_name = input('What is the updated client name ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The clienty is in the client\'s list')
        else:
            print('The client: {} is not in our clinet\'s list' .format(client_name))   # las {} es un placeholder que permite poner nuevos valores con posterioridad, lo que permite adicionarles es el .format(variable_que_tiene_los_valores_a_adicionar)
    else:
        print('Invalid command')



