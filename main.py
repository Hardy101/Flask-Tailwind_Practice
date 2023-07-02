from flask import Flask, render_template, url_for, request
from api import API
from day_and_month import day_today, month_name

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    location = request.args.get('location')  # Value from the Input in form
    date = {
        "today": day_today,
        'month_name': month_name
    }
    if location:
        api = API(query=location)
        data = api.weather_data()
        return render_template('index.html', data=data, date=date)
    else:
        return render_template('index.html', data=None, icon='static/css/img/img_1.png', date=date)


if __name__ == '__main__':
    app.run(debug=True)
