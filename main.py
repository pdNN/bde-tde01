import argparse
from src.utils import get_mongo_database


def main(mongo: object):
    """
        main faz todo o fluxo do tde, conecta ao banco, faz os devidos inserts
        da updates, remove alguns registros e lista-os

        :mongo: object: objeto contendo 

        :return: object: retorna a listagem final
    """

    # Entrando na database
    tde01_db = get_mongo_database(username=mongo['username'],
                                  password=mongo['password'],
                                  host=mongo['host'],
                                  database=mongo['database'])

    # Criar tabelas
    turmas = tde01_db["turmas"]

    item_1 = {"_id": "3", "turma": "Teste 3"}

    item_2 = {
        "_id": "4",
        "item_name": "Teste 4",
    }
    turmas.insert_many([item_1, item_2])


if __name__ == "__main__":
    """
        execução direta do arquivo
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
