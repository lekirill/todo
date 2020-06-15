import datetime as dt
import ujson

from flask import request, Response
from app import db
from models import Tasks


def prepare_task_data(task):
    return {
        'header': task.header,
        'description': task.description,
        'date_posted ': str(task.date_posted),
        'is_done': task.is_done,
    }


def setup_app(app):
    @app.route('/', methods=['GET'])
    def main():
        """
        Just main
        :return:
        """
        return Response(
            ujson.dumps(dict(hello='todo app')),
            status=200,
            mimetype='application/json')

    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        """
        Health check for container. Usually check db connection
        :return:
        """
        try:
            eng = db.get_engine()
            return Response(
                ujson.dumps(dict(status='OK')),
                status=200,
                mimetype='application/json')
        except:
            return Response(
                ujson.dumps(dict(status=f'Error')),
                status=400,
                mimetype='application/json')

    @app.route('/tasks/', methods=['GET'])
    def get_all_tasks():
        """
        Get all tasks
        :return:
        """
        tasks = db.session.query(Tasks).all()
        tasks_to_return = {}
        for task in tasks:
            tasks_to_return[task.id] = prepare_task_data(task)
        db.session.commit()
        return Response(
            ujson.dumps(tasks_to_return),
            status=200,
            mimetype='application/json')

    @app.route('/add/', methods=['POST'])
    def create_task():
        """
        Add new task to list
        :return:
        """
        data = request.get_json()
        header = data['header']
        description = data['description']
        if header:
            new_task = Tasks(header=header,
                             description=description,
                             date_posted=dt.datetime.now(),
                             )
            db.session.add(new_task)
            db.session.commit()
            return Response(
                ujson.dumps(dict(message=f'Task was added')),
                status=200,
                mimetype='application/json')
        else:
            return Response(
                ujson.dumps(dict(message=f'Task was not added. Payload is not suitable')),
                status=400,
                mimetype='application/json')

    @app.route('/get_task/', methods=['GET'])
    def get_task():
        """
        Get task by id
        :return:
        """
        task_id = request.args.get('id')
        if str(task_id).isnumeric():
            task = db.session.query(Tasks).get(task_id)
            if task:
                task_to_return = prepare_task_data(task)
                db.session.commit()
                return Response(
                    ujson.dumps(task_to_return),
                    status=200,
                    mimetype='application/json')
            else:
                return Response(
                    ujson.dumps(dict(error=f'No task with id {task_id}')),
                    status=400,
                    mimetype='application/json')
        else:
            return Response(
                ujson.dumps(dict(error=f'id should be numeric')),
                status=400,
                mimetype='application/json')

    @app.route('/delete/', methods=['DELETE'])
    def delete_task():
        """
        Delete task by id
        :return:
        """
        task_id = request.args.get('id')
        if str(task_id).isnumeric():
            db.session.query(Tasks).filter(Tasks.id == task_id).delete()
            db.session.commit()
            return Response(
                ujson.dumps(dict(Message=f'Task {task_id} deleted')),
                status=400,
                mimetype='application/json')
        else:
            return Response(
                ujson.dumps(dict(error=f'id should be numeric')),
                status=400,
                mimetype='application/json')

    @app.route('/update/', methods=['PUT'])
    def update_task():
        """
        Update task by id
        :return:
        """
        task_id = request.args.get('id')
        data = request.get_json()
        header = data['header'] if 'header' in dict(data).keys() else None
        description = data['description'] if 'description' in dict(data).keys() else None
        if str(task_id).isnumeric():
            task = db.session.query(Tasks).get(task_id)
            if task:
                if header:
                    task.header = header
                if description:
                    task.description = description
                db.session.commit()
                return Response(
                    ujson.dumps(dict(Message=f'Task {task_id} was updated')),
                    status=200,
                    mimetype='application/json')
            else:
                return Response(
                    ujson.dumps(dict(error=f'No task with id {task_id}')),
                    status=400,
                    mimetype='application/json')
        else:
            return Response(
                ujson.dumps(dict(error=f'id should be numeric')),
                status=400,
                mimetype='application/json')

    @app.route('/done/', methods=['PUT'])
    def set_done():
        """
        Set task done
        :return:
        """
        task_id = request.args.get('id')
        if str(task_id).isnumeric():
            task = db.session.query(Tasks).get(task_id)
            task.is_done = True
            db.session.commit()
            return Response(
                ujson.dumps(dict(Message=f'Task {task_id} is done!')),
                status=200,
                mimetype='application/json')
        else:
            return Response(
                ujson.dumps(dict(error=f'id should be numeric')),
                status=400,
                mimetype='application/json')

    return app
