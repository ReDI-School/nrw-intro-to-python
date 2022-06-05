from dataclasses import asdict
from unittest import mock, TestCase

from fastapi.testclient import TestClient

import api


class TestListItem(TestCase):
    def test_constructor_completed(self):
        instance = api.ListItem(title='test')
        self.assertEqual(instance.title, 'test')
        self.assertEqual(instance.completed, False)

    def test_constructor_completed_status_specified(self):
        instance = api.ListItem(title='test', completed=True)
        self.assertEqual(instance.title, 'test')
        self.assertEqual(instance.completed, True)

class TestAPI(TestCase):
    # Ahead of every test, create a new test client
    def setUp(self):
        # create test client
        self.client = TestClient(api.app)
        
    def test_docs_endpoint(self):
        response = self.client.get('/docs')
        self.assertEqual(response.status_code, 200)

    def test_list_items(self):
        response = self.client.get('/')
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)
        # Check that 2 entries were provided
        self.assertEqual(len(response.json()), 2)
        # Check that both entries have all expected fields
        for item in response.json():
            self.assertTrue({'title', 'uid', 'completed'}.issubset(set(item.keys())))
    
    @mock.patch.object(api, 'todo_list', [])
    def test_add_item_default_completion_status(self):
        response = self.client.post(
            '/add',
            json={"title": "Create POST endpoint"}
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)
        new_task_uid = response.json()
        
        # Check that list endpoint now returns 1 task
        response = self.client.get('/')
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['uid'], str(new_task_uid))
        self.assertEqual(response.json()[0]['completed'], False)
    
    @mock.patch.object(api, 'todo_list', [])
    def test_add_item_completion_status_set(self):
        response = self.client.post(
            '/add',
            json={"title": "Create POST endpoint", "completed": True}
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)
        new_task_uid = response.json()
        
        # Check that list endpoint now returns 1 task
        response = self.client.get('/')
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['uid'], str(new_task_uid))
        self.assertEqual(response.json()[0]['completed'], True)
        
    @mock.patch.object(api, 'todo_list', [api.ListItem(title='Test')])
    def test_delete_item(self):
        # Read out UID of list item
        item_uid = api.todo_list[0].uid
        # Delete item through API call
        response = self.client.delete(
            f'/delete/{item_uid}',
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)

        # Check that list endpoint now returns 0 tasks
        response = self.client.get('/')
        self.assertEqual(len(response.json()), 0)
    
    @mock.patch.object(api, 'todo_list', [api.ListItem(title='Test')])
    def test_delete_item(self):
        # Read out UID of list item
        item_uid = api.todo_list[0].uid
        # Delete item through API call
        response = self.client.delete(
            f'/delete/{item_uid}',
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)

        # Check that list endpoint now returns 0 tasks
        response = self.client.get('/')
        self.assertEqual(len(response.json()), 0)
        
    @mock.patch.object(api, 'todo_list', [api.ListItem(title='Test')])
    def test_mark_item_complete_changes_completed_flag(self):
        # Read out UID of list item
        item_uid = api.todo_list[0].uid
        # Check that item is currently not completed
        self.assertEqual(api.todo_list[0].completed, False)
        # Delete item through API call
        response = self.client.patch(
            f'/complete/{item_uid}',
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)

        # Check that list endpoint now returns 1 tasks
        response = self.client.get('/')
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['uid'], item_uid)
        # Check that completion status is now True
        self.assertEqual(response.json()[0]['completed'], True)
    
    @mock.patch.object(api, 'todo_list', [api.ListItem(title='Test')])
    def test_mark_item_complete_returns_item(self):
        # Read out UID of list item
        item_uid = api.todo_list[0].uid
        # Check that item is currently not completed
        self.assertEqual(api.todo_list[0].completed, False)
        # Delete item through API call
        response = self.client.patch(
            f'/complete/{item_uid}',
        )
        # Check that server responded with status code 200
        self.assertEqual(response.status_code, 200)

        # Check that the returned item is as expected.
        self.assertTrue({'title', 'uid', 'completed'}.issubset(set(response.json().keys())))
        self.assertEqual(response.json()['uid'], item_uid)
        self.assertEqual(response.json()['completed'], True)
        
    