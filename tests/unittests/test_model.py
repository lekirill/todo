import unittest
import datetime as dt

from models import Tasks


class TaskPrepareTests(unittest.TestCase):

    def test_prepare_task_data(self):
        task = Tasks(header='test',
                     description='test_desc',
                     date_posted='2020-06-14 19:37:54.609570',
                     is_done=False
                     )
        print(task.date_finished)
        self.assertTrue(
            task.is_done == False and
            task.header == 'test' and
            task.description == 'test_desc' and
            task.date_posted == '2020-06-14 19:37:54.609570'
        )


if __name__ == '__main__':
    unittest.main()
