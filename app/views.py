from app import app
from app.models.product import Product
from flask import render_template, redirect, url_for, request
from os import listdir
from flaskext.markdown import Markdown
from app.wtforms import WTForms
import pandas as pd

# flask służy do pisania wersji obiektowej aplikacji
Markdown(app)
app.config["SECRET_KEY"] = "123"

@app.route('/')
@app.route('/index')
def index(): 
    readme = ""
    with open("README.md", 'r', encoding="UTF-8") as f:
        readme = f.read()
    return render_template("index.html.jinja", text=readme)

@app.route('/extract', methods=['GET', 'POST'])
def extract():
    form=WTForms()
    if form.validate_on_submit():
        if request.method == 'POST':
            product_id =request.form.get('product_id')
            product = Product(product_id, opinions=[])
            product.extract_product()
            product.save_to_json()
            return redirect(url_for('opinions', product_id=product_id, form=form ))
    return render_template("extract.html.jinja", form=form)

@app.route('/products')
def products():
    products_list = [product.split('.')[0] for product in listdir("app/products")]
    return render_template("products.html.jinja", products=products_list)

@app.route('/opinions/<product_id>')
def opinions(product_id):
    headings=("opinion_id","recommendation","stars","content","pros","cons","purchased","submit_date","purchase_date","useful","useless")
    print(product_id)
    product = Product(product_id, opinions=[])
    print(", ".join(op.opinion_id for op in product.opinions))
    product.read_from_json()
    #----------------------------------------------- PRÓBA STWORZENIA TABELI -------------------------------------------------------------
    prod=product.opinions
    opinionsFormated = pd.DataFrame.from_records([opinion.to_dict() for opinion in prod])
    # prod=""
    # prod=product.read_from_json()
    # opinionsFormated = pd.DataFrame.from_records(prod.to_dict()) #from_dict nie działa
    return render_template("opinions.html.jinja", product=str(product), headings=headings, opinionsFormated=opinionsFormated.to_html())

@app.route('/charts/<product_id>')
def charts(product_id):
    pass

@app.route('/about')
def about():
    aboutme = ""
    with open("ABOUTME.md", 'r', encoding="UTF-8") as f:
        aboutme = f.read()
    return render_template("about.html.jinja", text=aboutme)
    