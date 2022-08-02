from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success_table', methods=['POST'])
def success_table():
    if request.method == 'POST':
        file = request.files['file']
        df = pandas.read_csv(file)
        gc = Nominatim(user_agent="my-flask-app")
        df["coodrinates"] = df["Address"].apply(gc.geocode)
        df['Latitude'] = df['coodrinates'].apply(
            lambda x: x.latitude if x != None else None)
        df['Longitude'] = df['coodrinates'].apply(
            lambda x: x.longitude if x != None else None)
        df = df.drop('coordinates', 1)
        df.to_csv('uplaods/geocoded.csv', index=None)
        return render_template('index.html', text=df.to_html(), btn="download.html")


@app.route('/download_file')
def download_file():
    return send_file("uplaods/geocoded.csv", attachment_filename='yourfile.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
