import asyncio

from flask import Flask, render_template, redirect, url_for

from db.db_manager import Database

app = Flask(__name__)
db = Database(["db", "database.db"])

@app.route('/')
@app.route('/home')
async def hello_world():
    return render_template("index.html", title="Sushi App | Home", navi_status="home")

@app.route('/menu')
async def menu():
    menu_items = await db.menu_items()
    return render_template("menu.html", title="Sushi App | Menu", navi_status="menu", menu_items=menu_items)

@app.route('/menu/<item_name>')
async def item(item_name):
    menu_item = await db.menu_item(item_name)
    
    if menu_item is not None:
        return render_template("item_page.html", title=f"Sushi App | {menu_item[0]}", navi_status="menu", status_bar="white", menu_item=menu_item)
    else:
        return redirect('/menu')
    
@app.route('/basket')
async def basket():
    menu_items = await db.menu_items()
    return render_template("basket.html", title="Sushi App | Basket", navi_status="basket", menu_items=menu_items)

if __name__ == '__main__':
    app.run(port="7777", debug=True)
