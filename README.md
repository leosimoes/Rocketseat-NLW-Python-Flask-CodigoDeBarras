# Rocketseat - NLW - Python - Flask - Barcode

Rocketseat's NLW event project using Python and Flask to generate barcode.

## Steps
1. Create Flask project in PyCharm:

![Image-1-PyCharm-InitProject](imgs/Img-1-PyCharm-Init.jpg)

2. Install other dependencies:
- pillow
- python-barcode

3. Change `app.py`:
- remove route `/`;
- add route `POST '/create_tag'` which receives "product_code" and creates an image in the program folder;

4. Test route `http://127.0.0.1:5000/create_tag` with Postman passing ```{"tag path": "987-654-321"}```;

![imgs/Img-2-Test-987-654-32](imgs/Img-2-Test-987-654-321.jpg)

5. Create directories:
- from the project root: `/src`, `/src/controllers`, `/src/drivers`, `/src/errors`, `/src/main`,
   `/src/main/routes`, `/src/main/server`, `/src/validators`, `/src/views`, `/src/views/http_types`
- everyone must have a `__init__.py` file
