from app import app
from app.models.product import Product

@app.route('/')
@app.route('/index')
def index():
    return "helloooooo"

@app.route('/extract/<product_id>')
def extract(product_id):
    product = Product(product_id)
    product.extract_product()
    product.save_to_json(product_id)
    return str(product)


@app.route('/products')
def products():
    pass

@app.route('/opinions/<productId>')
def opinions(productId):
    pass

@app.route('/charts/<productId>')
def charts(productId):
    pass
