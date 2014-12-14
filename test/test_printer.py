from unittest import TestCase

from mock import call, patch

from deepest import printer


EXPECTATIONS = [
    'breadth of dirs examined    longest pathname    deepest directory',
    '                       1                  12                  123',
    'longest file: longest_file',
    'deepest path: deepest_path'
]


class printer_BaseCase(TestCase):
    def setUp(self):
        self.write_mock = patch.object(printer.sys.stdout, 'write').start()


class print_header_TestCase(printer_BaseCase):
    def test_print_header(self):
        printer.print_header()
        self.write_mock.assert_called_once_with(
            EXPECTATIONS[0] + printer.linesep)


class print_update_TestCase(printer_BaseCase):
    def setUp(self):
        super(print_update_TestCase, self).setUp()
        self.stdout_content = ''

        def concatenator(data):
            self.stdout_content += data

        self.write_mock.side_effect = concatenator

    def test_print_update(self):
        printer.print_update('1', '12', '123')
        self.assertEqual(
            '\r' + EXPECTATIONS[1],
            self.stdout_content)


class print_footer_TestCase(printer_BaseCase):
    def test_print_footer(self):
        printer.globals.longest_file = 'longest_file'
        printer.globals.deepest_path = 'deepest_path'
        printer.print_footer()
        self.write_mock.assert_has_calls([
            call(printer.linesep + printer.linesep),
            call(EXPECTATIONS[2] + printer.linesep),
            call(EXPECTATIONS[3] + printer.linesep)
        ])
