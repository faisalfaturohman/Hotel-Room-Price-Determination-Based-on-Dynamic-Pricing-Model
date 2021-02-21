import warnings
warnings.filterwarnings('ignore')
from werkzeug.exceptions import HTTPException

from flask import Flask, request, render_template, abort,send_file
from  werkzeug.debug import get_current_traceback

import os
import pandas as pd
import joblib

app = Flask(__name__)
application = app
SECRET_KEY = 'coba'

@app.errorhandler(500)
def internal_error(error):

    return render_template('error.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')

@app.route("/", methods=['GET', 'POST'])
def index():    
    if request.method == 'POST':                               
        date = request.form['date']
        tanggal = pd.to_datetime(date).day
        bulan = pd.to_datetime(date).month
        tahun = pd.to_datetime(date).year
        lama_menginap = request.form['lama_menginap']
        jenis_kamar = request.form['jenis_kamar']
        status_hari = request.form['status_hari'] 
        demand = request.form['demand']
        loaded_model = joblib.load('static/model.pkl')
        df = pd.DataFrame({
            'Lama_menginap': lama_menginap,
            'Tanggal': tanggal,
            'Bulan': bulan,
            'Tahun': tahun,
            'Jenis Kamar': jenis_kamar,
            'Hari': status_hari,
            'Demand': demand}, index=[0])        
        harga_prediksi = loaded_model.predict(df)        
        harga_prediksi = ''.join(str(e) for e in harga_prediksi)
        return render_template('index.html',harga_prediksi=harga_prediksi)	
    return render_template('index.html')	

if __name__ == '__main__':
    app.run(debug=False)
