from flask import Flask, render_template, request, redirect
from find.geolocate import locate

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

##--INDEX--##
@app.route('/')
def home():
    lijst = locate(['10.24.193.110', '91.183.242.146', '91.183.242.116', '91.183.245.122', '108.170.241.193', '108.170.227.3', '172.217.168.206'])
    return render_template('index.html', iplijst = lijst)

##--CONFIG--##
if __name__ == '__main__':
    app.run(host='0.0.0.0')