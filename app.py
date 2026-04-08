from flask import Flask, render_template
from questions import questions_data

app = Flask(__name__)

@app.route('/')
def index():
    # Shows ALL questions on the home page
    return render_template('index.html', questions=questions_data)

@app.route('/unit/<int:unit_id>')
def view_unit(unit_id):
    # This creates a new list containing ONLY questions for the clicked unit
    filtered_questions = [q for q in questions_data if q['unit'] == unit_id]
    return render_template('index.html', questions=filtered_questions, current_unit=unit_id)

if __name__ == '__main__':
    app.run(debug=True, port=5001)