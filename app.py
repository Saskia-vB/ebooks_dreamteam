from flask import Flask, render_template, url_for, redirect, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a76hfb34ls9u6ty6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class CreateBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3,max=20)])
    author = StringField('Author', validators=[DataRequired(), Length(min=3,max=20)])
    submit = SubmitField('Create eBook')


# eBook class
class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"('{self.id}', '{self.title}', '{self.author}')"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/create_ebook', methods=['POST', 'GET'])
def create_ebook():
    form = CreateBookForm()
    if form.validate_on_submit():
        book = Ebook(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        flash(f'{form.title.data} has been added to the database!', 'success')
        return redirect('home')
    return render_template('create_ebook.html', form=form)


# debug mode
if __name__ == '__main__':
    app.run(debug=True)
