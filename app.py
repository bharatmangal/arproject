from flask import Flask, render_template
import time

app = Flask(__name__)

class StepCounter:
    def __init__(self):
        self.steps = 0

    def increment_steps(self):
        self.steps += 1
        return self.steps

    def reset_steps(self):
        self.steps = 0
        return self.steps

step_counter = StepCounter()

@app.route('/')
def index():
    return render_template('index.html', steps=step_counter.steps)

@app.route('/reset', methods=['POST'])
def reset():
    step_counter.reset_steps()
    return render_template('index.html', steps=step_counter.steps)

@app.route('/increment', methods=['POST'])
def increment():
    step_counter.increment_steps()
    return render_template('index.html', steps=step_counter.steps)

if __name__ == "__main__":
    app.run(debug=True)