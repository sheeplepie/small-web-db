from flask import Flask, render_template_string, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/data'
mongo = PyMongo(app)

HTML = '''
<html>
<head><title>Store Stuff</title></head>
<body>
    <h2>Docker-Compose example - Store Stuff</h2>
    <form>
        Store some stuff: 
        <input type="text" name="stuff">
        <input type="submit">
    </form>
    <table>
    {% for item in items %}
    <tr>
        <td>{{ item['data'] }}</td>
    </tr>
    {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def hello():
    data = request.args.get('stuff')
    if data:
        mongo.db.stuff.insert_one({'data': data})

    items = mongo.db.stuff.find()
    return render_template_string(HTML, items=items)

app.run(host='0.0.0.0', port=80)
