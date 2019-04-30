# -*- coding:utf-8 -*-   Date   : '2015/8/12 0012 * 10:55'
import os, time
from flask import request, flash, redirect, url_for, send_from_directory, session, render_template, Flask
from app import app




@app.route('/')
@app.route('/index/')
def user_index():
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)
