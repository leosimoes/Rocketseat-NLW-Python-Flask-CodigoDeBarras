from flask import request, jsonify, Blueprint
from barcode.codex import Code128
from barcode.writer import ImageWriter

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():  # put application's code here
    body = request.json
    product_code = body.get('product_code')
    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    return jsonify({'tag path': path_from_tag})
