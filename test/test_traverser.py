from unittest import TestCase

from mock import patch

from deepest import traverser

sep = traverser.os.path.sep


class traversal_callback_TestCase(TestCase):
    def setUp(self):
        self.update_mock = patch.object(traverser, 'print_update').start()
        traverser.globals.breadth = 0
        traverser.globals.now_length = traverser.globals.now_depth = 0
        traverser.globals.max_length = traverser.globals.max_depth = 0
        traverser.globals.longest_file = traverser.globals.deepest_path = ''
        traverser.globals.runas_program = False

    def test_traversal_callback_with_files(self):
        traverser.traversal_callback(
            None, 'dir' + sep + 'sub', ['file', 'longfile'])
        self.assertEqual(1, traverser.globals.breadth)
        self.assertEqual(16, traverser.globals.now_length)
        self.assertEqual(16, traverser.globals.max_length)
        self.assertEqual(1, traverser.globals.now_depth)
        self.assertEqual(1, traverser.globals.max_depth)
        self.assertEqual(
            sep.join(['dir', 'sub', 'longfile']),
            traverser.globals.longest_file)
        self.assertEqual('dir' + sep + 'sub', traverser.globals.deepest_path)
        self.assertFalse(self.update_mock.called)

    def test_traversal_callback_without_files(self):
        traverser.traversal_callback(None, 'dir' + sep + 'sub', [])
        self.assertEqual(1, traverser.globals.breadth)
        self.assertEqual(7, traverser.globals.now_length)
        self.assertEqual(7, traverser.globals.max_length)
        self.assertEqual(1, traverser.globals.now_depth)
        self.assertEqual(1, traverser.globals.max_depth)
        self.assertEqual(
            sep.join(['dir', 'sub']),
            traverser.globals.longest_file)
        self.assertEqual('dir' + sep + 'sub', traverser.globals.deepest_path)
        self.assertFalse(self.update_mock.called)

    def test_traversal_callback_runas_program(self):
        traverser.globals.runas_program = True
        traverser.traversal_callback(None, 'dir' + sep + 'sub', ['file'])
        self.assertEqual(1, traverser.globals.breadth)
        self.assertEqual(12, traverser.globals.now_length)
        self.assertEqual(12, traverser.globals.max_length)
        self.assertEqual(1, traverser.globals.now_depth)
        self.assertEqual(1, traverser.globals.max_depth)
        self.assertEqual(
            sep.join(['dir', 'sub', 'file']),
            traverser.globals.longest_file)
        self.assertEqual('dir' + sep + 'sub', traverser.globals.deepest_path)
        self.update_mock.assert_called_once_with(1, 12, 1)

    def test_traversal_callback_non_incrementing_case_with_files(self):
        traverser.globals.max_length = 99
        traverser.globals.max_depth = 99
        traverser.traversal_callback(
            None, 'dir' + sep + 'sub', ['file', 'longfile'])
        self.assertEqual(1, traverser.globals.breadth)
        self.assertEqual(99, traverser.globals.now_length)
        self.assertEqual(99, traverser.globals.max_length)
        self.assertEqual(99, traverser.globals.now_depth)
        self.assertEqual(99, traverser.globals.max_depth)
        self.assertEqual('', traverser.globals.longest_file)
        self.assertEqual('', traverser.globals.deepest_path)
        self.assertFalse(self.update_mock.called)

    def test_traversal_callback_non_incrementing_case_without_files(self):
        traverser.globals.max_length = 99
        traverser.globals.max_depth = 99
        traverser.traversal_callback(
            None, 'dir' + sep + 'sub', [])
        self.assertEqual(1, traverser.globals.breadth)
        self.assertEqual(99, traverser.globals.now_length)
        self.assertEqual(99, traverser.globals.max_length)
        self.assertEqual(99, traverser.globals.now_depth)
        self.assertEqual(99, traverser.globals.max_depth)
        self.assertEqual('', traverser.globals.longest_file)
        self.assertEqual('', traverser.globals.deepest_path)
        self.assertFalse(self.update_mock.called)
