

clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    clients += client_name
    _add_coma()


def _add_coma():
    global clients

    clients += ","


if __name__ == '__main__':
    create_client('David')
    print(clients)

