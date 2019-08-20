#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def index():
    return "Hello"


@app.route('/restaurantMenu/<int:restaurant_id>/create', methods=['GET', 'POST'])
def create(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)

    if request.method == 'POST':
        new_item = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(new_item)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('read_restaurant', restaurant_id=restaurant_id))
    else:
        return render_template("/restaurant/menu/create.html", restaurant=restaurant)


@app.route('/restaurantMenu/<int:restaurant_id>/<int:item_id>/read')
def read(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    item = session.query(MenuItem).filter_by(item_id=item_id)
    return render_template("/restaurant/menu/read.html", restaurant=restaurant, item=item)


@app.route('/restaurantMenu/<int:restaurant_id>/read')
def read_restaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template("/restaurant/read.html", restaurant=restaurant, items=items)


@app.route('/restaurantMenu/<int:restaurant_id>/<int:item_id>/update', methods=['GET', 'POST'])
def update(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    item = session.query(MenuItem).filter_by(id=item_id)

    if request.method == 'POST':
        item.name = request.form['name']
        session.add(item)
        session.commit()
        flash("menu item edited!")
        return redirect(url_for('read_restaurant', restaurant_id=restaurant_id))
    else:
        return render_template("/restaurant/menu/update.html", restaurant=restaurant, item=item)


@app.route('/restaurantMenu/<int:restaurant_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def delete(restaurant_id, item_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id)
    item = session.query(MenuItem).filter_by(id=item_id)

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash("menu item deleted!")
        return redirect(url_for('read_restaurant', restaurant_id=restaurant_id))
    else:
        return render_template("/restaurant/menu/delete.html", restaurant=restaurant, item=item)


def main():
    # app.secret_key = "It is a secret."
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
