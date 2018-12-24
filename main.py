import shouty

params = {
    'host': 'localhost',
    'port': 8000,
    'user': 'source',
    'password': 'cuban',
    'format': shouty.Format.OGG,
    'mount': '/shouty'
}

with shouty.connect(**params) as connection:
    connection.send_file('playlist/edbnao.ogg')


with shouty.connect(**params) as connection:
    with open('./whitenoise.ogg', 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break

            connection.send(chunk)
            connection.sync()

    with open('./playlist/edbnao.ogg', 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break

            connection.send(chunk)
            connection.sync()
