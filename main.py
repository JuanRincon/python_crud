

clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    clients += (client_name)

if __name__ == '__main__':
    create_client('David')
    print(clients)

