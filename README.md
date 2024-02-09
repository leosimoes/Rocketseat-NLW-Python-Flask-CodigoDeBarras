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

![imgs/Img-3-Directories.jpg](imgs/Img-3-Directories.jpg)

6. Extract part of the code from `app.py` to
- `server.py`: creates app and registers Blueprints
- `tag_routes.py`: creates a Blueprint for the `POST '/create_tag'` route

7. Extract part of the `create_tag` function code from `tag_routes.py` to the files:
- `src.drivers.barcode_handler.py` with the BarcodeHandler class;
- `src/views/tag_creator_view.py` with the TagCreatorView class;
- `src.controllers.tag_creator_controller.py` with the TagCreatorController class;
- `src.views.http_types.http_request.py` with the HttpRequest class;
- `src.views.http_types.http_response.py` with the HttpResponse class.
