from app import app, db
from flask import render_template, request, flash, redirect, url_for
from .forms import FRM_PAGE
from .models import TBL_POST

@app.route('/master')
def master():
    return render_template('master.html')

@app.route('/extended')
def extended():
    form = FRM_PAGE()
    return render_template('extended.html', form=form)

@app.route('/showMessage', methods=['GET','POST'])
def showMessage():
    form = FRM_PAGE()
    if request.method == 'POST':
        if form.validate_on_submit():
            post = TBL_POST(title=form.title.data,content=form.content.data)
            db.session.add(post)
            db.session.commit()
            flash("Add Post Successfully!","Success")
    return redirect(url_for('homepage'))

@app.route('/home') 
def homepage():
    tblpost = TBL_POST.query.all()
    return render_template('home.html', tblpost=tblpost)
