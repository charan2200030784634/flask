from flask import Flask, render_template, request, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def load_results():
    try:
        with open('data/results.json', 'r') as file:
            results = json.load(file)
    except FileNotFoundError:
        results = []
    return results

def save_results(results):
    with open('data/results.json', 'w') as file:
        json.dump(results, file)

@app.route('/')
def index():
    results = load_results()
    return render_template('index.html', results=results)

@app.route('/add_result', methods=['GET', 'POST'])
def add_result():
    if request.method == 'POST':
        name = request.form['name']
        score = request.form['score']

        if not name or not score:
            flash('Name and Score are required!', 'error')
        else:
            results = load_results()
            results.append({'name': name, 'score': score})
            save_results(results)
            flash('Result added successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('add_result.html')

if __name__ == '__main__':
    app.run(debug=True)
