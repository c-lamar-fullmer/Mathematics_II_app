from flask import Flask, render_template
from questions import questions_data

app = Flask(__name__)

@app.route('/')
def index():
    # It's good practice to pass None for current_unit explicitly 
    return render_template('index.html', questions=questions_data, current_unit=None)

@app.route('/unit/<int:unit_id>')
def view_unit(unit_id):
    filtered_questions = [q for q in questions_data if q.get('unit') == unit_id]
    return render_template('index.html', questions=filtered_questions, current_unit=unit_id)

if __name__ == '__main__':
    app.run(debug=True, port=5002)