#!/usr/bin/env python3
# src/products.py
import os
from storage import read_csv, write_csv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.csv')
FIELDS = ['product_id','name','price','stock']


def list_products():
    return read_csv(PRODUCTS_FILE)


def find_product(pid):
    for p in list_products():
        if p.get('product_id') == pid:
            return p
    return None


def add_product(product):
    rows = list_products()
    rows.append(product)
    write_csv(PRODUCTS_FILE, FIELDS, rows)


def update_stock(pid, new_stock):
    rows = list_products()
    for r in rows:
        if r.get('product_id') == pid:
            r['stock'] = str(new_stock)
    write_csv(PRODUCTS_FILE, FIELDS, rows)
