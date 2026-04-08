from flask import Flask, render_template

app = Flask(__name__)

# Note: We use \( \) for inline math and \[ \] for block math
questions_data = [
    {
        "id": 1, 
        "difficulty": "Easy",
        "question": "What is the truth value of \( P \lor \neg P \)?", 
        "answer": "This is a tautology, so it is always True."
    },
    {
        "id": 2, 
        "difficulty": "Medium",
        "question": "Express the sum of the first \( n \) integers using sigma notation.", 
        "answer": "\[ \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \]"
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)