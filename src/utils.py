from pymongo import MongoClient

def get_mongo_database(username: str, password: str, host: str, database: str):
    """
        get_mongo_database inicia a conexão com um banco de dados mongo e retorna
        essa conexão

        :username: str: usuário para conexão ao banco de dados mongo
        :password: str: senha para conexão ao banco de dados mongo
        :host: str: ip completo para conexão ao banco de dados mongo
        :database: str: banco de dados a ser conectado
        :return: MongoClient: banco de dados conectado
    """ 

    # URL de conexão mongo
    CONNECTION_STRING = f"mongodb://{username}:{password}@{host}"

    client = MongoClient(CONNECTION_STRING)

    # Retorna a collecion criada
    return client[database]