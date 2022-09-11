# TDE 01 - Document-Object Mapper com o MongoDB em Python
> Pedro Henrique Lucho

Script simples em Python para manipulação de um banco de dados em mongodb para o tde01 da matéria de Banco de Dados Evolucionários.

O script cria 3 collections, faz insert nas mesmas, da update em alguns registros, faz alguns selects e deleta alguns registros para testar o CRUD completo no banco.

Contexto: loja de carros

Print da execução:
![image](https://user-images.githubusercontent.com/26514016/189509431-21a044a3-65b5-4615-832a-1de380109058.png)

Requerimentos:
- python >= 3.8
- mongodb

Como executar:
- Em unix, executar os comandos:
    ```
    make clean
    make install
    python main.py <mongodb username> <mongodb password> <mongodb host> <mongodb database>
    (ex: python main.py root MongoDB2019! localhost:27017 tde01)
    ```

- Em windows executar os comandos:
    ```
    pip install virtualenv
    virtualenv venv
    .\venv\Scripts\Activate.ps1
    pip install -r ./requirements.txt
    python main.py <username> <password> <host> <database>
    ex: python main.py root MongoDB2019! localhost:27017 tde01
    ```

Estrutura:
- diretório inicial:
    - src
        - utils.py
        > Arquivo com as funções auxiliares do script principal
    - docker-compose.yaml
    > Instancia o banco de dados mongodb via docker na máquina
    - main.py
    > Arquivo principal do script python
    - Makefile
    > Arquivo com os comandos para baixar as dependências da aplicação
    - requirements.txt
    > Arquivo com as dependências do arquivo

