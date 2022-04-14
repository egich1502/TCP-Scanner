from unittest import TestCase
from TCP_Scanner import scan_port


class Test(TestCase):
    def test_scan_port(self):
        self.assertEqual(scan_port('www.google.com', 80, []), 80)
        self.assertEqual(scan_port('www.youtube.com', 443, []), 443)
