import argparse
from src.utils import get_mongo_database
from pymongo import ASCENDING as pymongo_ASCENDING


def main(mongo: object):
    """
        main faz todo o fluxo do tde, conecta ao banco, faz os devidos inserts
        da updates, remove alguns registros e lista-os

        :mongo: object: objeto contendo 

        :return: object: retorna a listagem final
    """

    '''
        Entrando na database
    '''
    tde01_db = get_mongo_database(username=mongo['username'],
                                  password=mongo['password'],
                                  host=mongo['host'],
                                  database=mongo['database'])
    '''
        Cria a collecion
    '''
    listagens = tde01_db["listagens"]


    '''
        Dropa todos os registros da collecion
    '''
    deletes = listagens.delete_many({})

    print(f'Tabela Limpa! Deletado {deletes.deleted_count} itens\n')


    '''
        Cria um index automático
    '''
    listagens.create_index([("_id", pymongo_ASCENDING)])

    
    '''
        Cria os objetos
    '''
    listagens_arr = [
        {
            "carro": {
                "nome": "Corsa",
                "marca": "Chevrolet",
                "ano": 2012
            },
            "loja": {
                "nome": "Carrão Multimarcas",
                "cidade": "Colombo",
                "estado": "Paraná"
            },
            "preco": 20000.00
        },
        {
            "carro": {
                "nome": "Gol",
                "marca": "Volkswagen",
                "ano": 1998
            },
            "loja": {
                "nome": "Só Clássicos",
                "cidade": "Curitiba",
                "estado": "Paraná"
            },
            "preco": 40000.00
        },
        {
            "carro": {
                "nome": "208",
                "marca": "Peugeot",
                "ano": 2014
            },
            "loja": {
                "nome": "Carrão Multimarcas",
                "cidade": "Colombo",
                "estado": "Paraná"
            },
            "preco": 44000.00
        },
        {
            "carro": {
                "nome": "BR-800",
                "marca": "Gurgel",
                "ano": 1991
            },
            "loja": {
                "nome": "Só Clássicos",
                "cidade": "Curitiba",
                "estado": "Paraná"
            },
            "preco": 28000.00
        },
        {
            "carro": {
                "nome": "SF90",
                "marca": "Ferrari",
                "ano": 2022
            },
            "loja": {
                "nome": "SuperCarros",
                "cidade": "Pinhais",
                "estado": "Paraná"
            },
            "preco": 1600000.00
        },
    ]

    creates = listagens.insert_many(listagens_arr)

    print(f'Criado {len(creates.inserted_ids)} itens\n')


    '''
        Query em um registro
    '''
    find_one = listagens.find_one()

    print(f'Query em um registro - {find_one["_id"]}:')
    print(find_one)
    print('------------------------')
    print('\n')


    '''
        Query em todos os registros
    '''
    find_all = listagens.find({})

    print(f'Todos os registros:')
    print(list(find_all))
    print('------------------------')
    print('\n')


    '''
        Atualiza o preço de uma listagem da loja Só Clássicos
    '''
    updated_arr = listagens.update_one({"carro.nome": "BR-800"},
                                       {"$set": {
                                           "preco": 28500.55
                                       }})

    print(f'Registro carro.nome = BR-800 alterado, resultado:')
    print(updated_arr.raw_result)
    print('------------------------')
    print('\n')


    '''
        Query em todos os registros na loja Só Clássicos
    '''
    find_soclassicos = listagens.find({"loja.nome": "Só Clássicos"})

    print(f'Listagens da loja Só Clássicos:')
    print(list(find_soclassicos))
    print('------------------------')
    print('\n')


    '''
        Query em todos os registros com preco superior a 100.000
    '''
    find_soclassicos = listagens.find({"preco": {"$gt": 100000}})

    print(f'Todos os registros com preco superior a 100.000:')
    print(list(find_soclassicos))
    print('------------------------')
    print('\n')


    '''
        Remove os registros com preco superior a 100.000
    '''
    deleted_arr = listagens.delete_many({"preco": {"$gt": 100000}})

    print(f'Registros com preco superior a 100.000 deletados, resultado:')
    print(deleted_arr.raw_result)
    print('------------------------')
    print('\n')


    '''
        Query em todos os registros com preco superior a 100.000
    '''
    find_soclassicos = listagens.find({"preco": {"$gt": 100000}})

    print(f'Todos os registros com preco superior a 100.000:')
    print(list(find_soclassicos))
    print('------------------------')
    print('\n')


if __name__ == "__main__":
    """
        Execução direta do arquivo
    """

    # Argumentos de conexão mongodb via parâmetro prompt
    parser = argparse.ArgumentParser("tde01-bde")

    parser.add_argument("username", help="Mongo Username", type=str)
    parser.add_argument("password", help="Mongo Password", type=str)
    parser.add_argument("host", help="Mongo Host", type=str)
    parser.add_argument("database", help="Mongo Database", type=str)

    args = parser.parse_args()

    username = args.username
    password = args.password
    host = args.host
    database = args.database

    # Executa a função principal passando os parâmetros
    main(
        mongo={
            'username': username,
            'password': password,
            'host': host,
            'database': database
        })
