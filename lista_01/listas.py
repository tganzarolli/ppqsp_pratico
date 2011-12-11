mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

def generate_tuple_list():
    tuple_list = [(h[0],h) for h in homens]
    return tuple_list
