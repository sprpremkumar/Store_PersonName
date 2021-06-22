from flask import Flask, redirect, url_for, request,render_template, flash, Blueprint
import json
import os.path

bp = Blueprint("Person_Name",__name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/details',methods=['GET','POST'])
def details():
    if request.method == 'POST':
        data ={}
        if os.path.exists('data.json'):
            with open('data.json') as datas_file:
                data = json.load(datas_file)

        if request.form['name'] in data.keys():
            flash('The Name is already Taken')
            return redirect(url_for('Person_Name.home'))

        data[request.form['name']]={'name':request.form['name']}
        with open('data.json','w') as data_file:
            json.dump(data,data_file,indent=1)
        return render_template('intro.html',name=request.form['name'])
    else:
        return redirect(url_for('Person_Name.home'))

