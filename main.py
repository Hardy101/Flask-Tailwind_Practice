from flask import Flask, render_template, url_for, request
from api import API
from day_and_month import day_today, month_name

app = Flask(__name__)


# location = 'Benin, Edo, NGN'
# api = API(query=location)
# data = api.weather_data()
# print(data)
@app.route("/", methods=['GET'])
def index():
    location = request.args.get('location')
    if location:
        api = API(query=location)
        data = api.weather_data()
        return render_template('index.html', data=data, today=day_today, month_name=month_name)
    else:
        return render_template('index.html', data=None, icon='static/css/img/img_1.png', today=day_today, month_name=month_name)


if __name__ == '__main__':
    app.run(debug=True)
