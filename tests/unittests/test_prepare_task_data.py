import unittest
import datetime as dt

from routes import prepare_task_data
from models import Tasks


class TaskPrepareTests(unittest.TestCase):

    def test_prepare_task_data(self):
        task = Tasks(header='test',
                     description='test_desc',
                     date_posted='2020-06-14 19:37:54.609570',
                     is_done=False
                     )
        validation_result = prepare_task_data(task)
        self.assertTrue(validation_result == {
            'header': 'test',
            'description': 'test_desc',
            'date_posted ': '2020-06-14 19:37:54.609570',
            'is_done': False
        })


if __name__ == '__main__':
    unittest.main()
