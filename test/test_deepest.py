from unittest import TestCase

from mock import patch

from deepest import deepest as deep


class deep_BaseCase(TestCase):
    def setUp(self):
        self.walk_mock = patch.object(deep, 'walk').start()

        def get_depth_effect(*args, **kwargs):
            deep.globals.deepest_path = 'deepest_path'
            deep.globals.max_depth = 12
            self.args = args
            self.kwargs = kwargs

        self.get_depth_effect = get_depth_effect

        def get_length_effect(*args, **kwargs):
            deep.globals.longest_file = 'longest_file'
            deep.globals.max_length = 12
            self.args = args
            self.kwargs = kwargs

        self.get_length_effect = get_length_effect


class get_depth_TestCase(deep_BaseCase):
    def test_get_depth(self):
        self.walk_mock.side_effect = self.get_depth_effect
        deepest_path, max_depth = deep.get_depth('.')
        self.walk_mock.assert_called_once_with(
            '.', deep.traversal_callback, '')
        self.assertEqual(3, len(self.args))
        self.assertEqual(('.', deep.traversal_callback, ''), self.args)
        self.assertEqual({}, self.kwargs)
        self.assertEqual('deepest_path', deepest_path)
        self.assertEqual(12, max_depth)


class get_length_TestCase(deep_BaseCase):
    def test_get_length(self):
        self.walk_mock.side_effect = self.get_length_effect
        longest_file, max_length = deep.get_length('.')
        self.walk_mock.assert_called_once_with(
            '.', deep.traversal_callback, '')
        self.assertEqual(3, len(self.args))
        self.assertEqual(('.', deep.traversal_callback, ''), self.args)
        self.assertEqual({}, self.kwargs)
        self.assertEqual('longest_file', longest_file)
        self.assertEqual(12, max_length)


class main_TestCase(TestCase):
    def setUp(self):
        self.footer_mock = patch.object(deep, 'print_footer').start()
        self.header_mock = patch.object(deep, 'print_header').start()
        self.sys_mock = patch.object(deep, 'sys').start()
        self.walk_mock = patch.object(deep, 'walk').start()
        self.write_mock = patch.object(deep.sys.stdout, 'write').start()

    def test_main_print_help(self):
        self.sys_mock.argv = ['', '-h']
        deep._main()
        self.assertTrue(deep.globals.runas_program)
        self.assertFalse(self.footer_mock.called)
        self.assertFalse(self.header_mock.called)
        self.assertFalse(self.walk_mock.called)
        self.write_mock.assert_called_once_with(
            deep.DESCRIPTION + deep.os.linesep)

    def test_main_print_for_current_dir(self):
        self.sys_mock.argv = ['']
        deep._main()
        self.assertTrue(deep.globals.runas_program)
        self.header_mock.assert_called_once_with()
        self.walk_mock.assert_called_once_with(
            '.', deep.traversal_callback, '')
        self.footer_mock.assert_called_once_with()
        self.assertFalse(self.write_mock.called)
