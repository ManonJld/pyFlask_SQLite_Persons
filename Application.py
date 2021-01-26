from flask import Flask, render_template, request, redirect, url_for, flash
import database
import os

app = Flask (__name__)
app.secret_key = os.environ['SECRET_KEY'] = 'testkey'
database.init_db()
import models

@app.route('/')
def page_index():
    personnes = models.Personne.query.all()
    return render_template('index.html', personnes=personnes)

@app.route('/addperson', methods=['GET', 'POST'])
def page_addperson():
    if request.method == 'POST':
        if not request.form['prenom'] or not request.form['nom'] or not request.form['email']:
            flash('Merci de remplir tous les champs', 'error')
        else:
            personne = models.Personne(request.form['nom'], request.form['prenom'],
                               request.form['email'])

            database.db_session.add(personne)
            database.db_session.commit()

            flash("L'enregistrement a bien été effectué")
            return redirect(url_for('page_index'))
    return render_template('addperson.html')

@app.route('/details/<idpersonne>', methods=['GET', 'POST'])
def page_detail(idpersonne):
    personne = models.Personne.query.filter(models.Personne.id == idpersonne).all()
    adresses = models.Adresse.query.filter(models.Adresse.personne_id == idpersonne).all()
#    print(personne)

    return render_template('details.html', id=idpersonne, personne=personne, adresses=adresses)

@app.route('/details/addaddress/<idpersonne>', methods=['GET', 'POST'])
def page_addaddress(idpersonne):
    if request.method == 'POST':
        if not request.form['rue'] or not request.form['cp'] or not request.form['ville'] or not request.form['personne_id'] or not request.form['typea']:
            flash('Merci de remplir tous les champs', 'error')
        else:
            adresse = models.Adresse(request.form['rue'], request.form['cp'],
                               request.form['ville'], request.form['personne_id'],
                               request.form['typea'])
            print(adresse)
            database.db_session.add(adresse)
            database.db_session.commit()

            flash("L'enregistrement a bien été effectué")
            return redirect(url_for('page_detail', idpersonne=idpersonne))
    return render_template('addaddress.html', id=idpersonne)