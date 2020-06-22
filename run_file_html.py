import os

from flask import Flask
from flask import render_template, url_for
from flask import request
from werkzeug.utils import redirect
from db_html_connect import ConnectHTMLSQL
import sqlite3

connection = sqlite3.connect('ebooks.db')
cursor = connection.cursor()

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "ebooksdb.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file


# class Book(ConnectHTMLSQL):

    # title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
all_tables = ConnectHTMLSQL().create_all_tables()

    # def __repr__(self):
    #     return "<title: {}>".format(self.title)


@app.route("/")
def render_static():
    return render_template("query_page.html")


# @app.route('/home', methods=['GET', 'POST'])
# def search():
#     # searchForm = searchForm()
#     # courses = models.Course.query
#     all_tables = ConnectHTMLSQL().create_all_tables()
#
#     # if all_tables.validate_on_submit():
#     #     names = all_tables.filter(all_tables.users.name.like('%' + all_tables.name.data + '%'))
#
#     # names = all_tables #.order_by(all_tables.users.name).all()
#
#     return render_template("query_page.html")
#
#
# @app.route('/search', methods=["GET", "POST"])
# def home():
#     all_tables = ConnectHTMLSQL().create_all_tables()
#         # try:
#         #     # all_tables.session.post()
#         #     # all_tables.session.get()
#         #     all_tables.session.add()
#         #     all_tables.session.commit()
#         # except Exception as e:
#         #     print("Failed to add book")
#         #     print(e)
#         #     all_tables.query.all()
#     return render_template("query_page.html")
#
#
#
#
# @app.route("/query_page", methods=["POST"])
# def add():
#     # try:
#     #     all_tables.form.get()
#     #     all_tables.form.get()
#     #     all_tables.query.filter_by(title='').first()
#     #     all_tables.session.commit()
#     # except Exception as e:
#     #     print("Couldn't update book title")
#     #     print(e)
#     return redirect("query_page.html")


# @app.route("/delete", methods=["POST"])
# def delete():
#     # all_tables.request.form.get()
#     # all_tables.query.filter_by(title='').first()
#     # all_tables.session.delete()
#     # all_tables.session.commit()
#     return redirect("home.html")


if __name__ == "__main__":
    app.run(debug=1, host='0.0.0.0')
