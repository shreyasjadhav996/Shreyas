from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Endpoint to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint to retrieve a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404

# Endpoint to update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.json.get('title', task['title'])
        task['description'] = request.json.get('description', task['description'])
        task['done'] = request.json.get('done', task['done'])
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}), 404

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run()
