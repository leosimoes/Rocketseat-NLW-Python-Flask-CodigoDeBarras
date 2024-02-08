# Rocketseat - NLW - Python - Flask - Código De Barras

Projeto do evento NLW da Rocketseat usando Python e Flask para gerar código de barras.

## Passos
1. Criar projeto Flask no PyCharm:

![Image-1-PyCharm-InitProject](imgs/Img-1-PyCharm-Init.jpg)

2. Instalar outras dependências:
- pillow
- python-barcode

3. Alterar `app.py`:
- remover rota `/`;
- adicionar rota `POST '/create_tag'` que recebe "product_code" e cria uma imagem na pasta do programa;

4. Testar rota `http://127.0.0.1:5000/create_tag` com Postman passando ```{"tag path": "987-654-321"}```;

![imgs/Img-2-Test-987-654-32](imgs/Img-2-Test-987-654-321.jpg)

5. Criar diretório `main` e subdiretórios `routes`e `server`
- todos devem ter um arquivo `__init__.py`
