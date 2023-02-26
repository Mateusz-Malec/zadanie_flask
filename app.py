from flask import Flask, jsonify, request
import sqlite3
import requests
import json

app = Flask(__name__)

# SQLite database initialization
conn = sqlite3.connect('todo.db', check_same_thread=False)
c = conn.cursor()


# c.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, description TEXT,
# completed BOOLEAN)')


# Endpoint for creating a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    title = request.json['title']
    description = request.json.get('description', '')
    completed = False
    c.execute("INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)", (title, description, completed))
    conn.commit()
    return jsonify({'status': 'success', 'message': 'Task created successfully'})


# Endpoint for getting all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for row in c.execute('SELECT * FROM tasks'):
        task = {'id': row[0], 'title': row[1], 'description': row[2], 'completed': row[3]}
        tasks.append(task)
    return jsonify({'status': 'success', 'tasks': tasks})


# Endpoint for getting a single task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = c.fetchone()
    if row is not None:
        task = {'id': row[0], 'title': row[1], 'description': row[2], 'completed': row[3]}
        return jsonify({'status': 'success', 'task': task})
    else:
        return jsonify({'status': 'error', 'message': 'Task not found'})


# Endpoint for updating a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    title = request.json.get('title', None)
    description = request.json.get('description', None)
    completed = request.json.get('completed', None)
    update_fields = {}
    if title is not None:
        update_fields['title'] = title
    if description is not None:
        update_fields['description'] = description
    if completed is not None:
        update_fields['completed'] = completed
    if not update_fields:
        return jsonify({'status': 'error', 'message': 'No fields to update'})
    update_query = ', '.join([f'{k} = ?' for k in update_fields])
    update_params = list(update_fields.values()) + [task_id]
    c.execute(f'UPDATE tasks SET {update_query} WHERE id = ?', update_params)
    conn.commit()
    return jsonify({'status': 'success', 'message': 'Task updated successfully'})


# Endpoint for deleting a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    return jsonify({'status': 'success', 'message': 'Task deleted successfully'})


if __name__ == '__main__':
    app.run()
