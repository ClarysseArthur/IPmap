from flask import Flask, render_template, request, redirect
from find.geolocate import locate
from find.get import getIP
from form import ipForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

##--INDEX--##


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ipForm()

    if form.is_submitted():
        ip = request.form.getlist('ipInput')
        addresses = getIP(ip[0])
        lijst = locate(addresses[2:])
    else:
        addresses = getIP('127.0.0.1')
        lijst = locate(addresses[2:])

    return render_template('index.html', iplijst=lijst, form=form)


##--CONFIG--##
if __name__ == '__main__':
    app.run(host='0.0.0.0')
