from flask import Flask, render_template
from questions import questions_data

app = Flask(__name__)

@app.route('/')
def index():
    # Setting current_unit to 0 to represent the "Show All" state
    return render_template('index.html', questions=questions_data, current_unit=0)

@app.route('/unit/<int:unit_id>')
def view_unit(unit_id):
    filtered_questions = [q for q in questions_data if q.get('unit') == unit_id]
    return render_template('index.html', questions=filtered_questions, current_unit=unit_id)

if __name__ == '__main__':
    # Running on port 5002 as per your current setup
    app.run(debug=True, port=5002)