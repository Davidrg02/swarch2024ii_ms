from flask import Blueprint, render_template, request, jsonify
from services.products_service import ProductService

product_blueprint = Blueprint('products', __name__)

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.form
        name = data.get('name')
        description = data.get('description')
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        ProductService.create_product(name, description)
        return jsonify({'message': 'Product created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        product = ProductService.update_product(product_id, name, description)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'message': 'Product updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_blueprint.route('/')
def index():
    return render_template('index.html')
