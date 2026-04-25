from flask import Flask, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    html = "<h1>DevOps To-Do List</h1><ul>"
    for i, t in enumerate(tasks):
        html += f"<li>{t} <a href='/delete/{i}'>[Delete]</a></li>"
    html += "</ul><form action='/add' method='POST'><input name='task' required><button>Add Task</button></form>"
    return html

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # host='0.0.0.0' is required so Docker can expose the port to your machine
    app.run(host='0.0.0.0', port=5000)