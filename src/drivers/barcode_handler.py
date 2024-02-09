from typing import Dict
from barcode.codex import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:

    def create_barcode(self, product_code: str):
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)

        return path_from_tag
