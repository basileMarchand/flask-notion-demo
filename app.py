from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

from notion_api import push_to_notion, pull_from_notion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_secret_key_ici'

class UserForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prenom', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    humeur = SelectField('Humeur', choices=[('heureux', 'Heureux'), ('triste', 'Triste')], validators=[DataRequired()])
    submit = SubmitField('Envoyer')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        mail = form.mail.data
        humeur = form.humeur.data
        # Envoi des données à Notion ici
        push_to_notion(nom, prenom, mail, humeur)
        return redirect(url_for('database'))
    return render_template('index.html', form=form)

@app.route('/database')
def database():
    donnees = pull_from_notion()
    return render_template('database.html', donnees=donnees)

if __name__ == '__main__':
    app.run(debug=True)
