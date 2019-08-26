#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)


@app.route('/restaurant/<int:restaurant_id>/menu/json')
def restaurantMenuJSON(restaurant_id):
    return "<body>restaurants menus API</body>"


@app.route('/item/<int:item_id>/json')
def restaurantMenuItemJSON(item_id):
    return "<body>restaurants menus items API</body>"


@app.route('/')
def index():
    return "Hello"


@app.route('/restaurantMenu/read')
def read():
    return "<body>restaurants page</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/read')
def read_restaurant():
    return "<body>a restaurant page</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/update')
def update_restaurant():
    return "<body>test</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/delete')
def delete_restaurant():
    return "<body>test</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/create')
def create_item():
    return "<body>test</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/<int:item_id>/update')
def update_item():
    return "<body>test</body>"


@app.route('/restaurantMenu/<int:restaurant_id>/<int:item_id>/delete')
def delete_item():
    return "<body>test</body>"


def main():
    app.secret_key = "It is a secret."
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
