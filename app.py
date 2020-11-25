from flask import Flask,render_template, redirect, url_for
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
# =======================================================

# BX-Books=pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding='latin-1')
# print(BX-Books.head())
# books['elo']=1200.0
# print(books.head())
# =========================================================

books = pd.read_csv('BX-Books.csv', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']
# ==========================================================


app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>hello {}</h1>'

# @app.route('/<name>')
# def index(name):
#     return '<h1>hello {}</h1>'.format(name)

@app.route("/")
def home():
    return render_template("home.html")


