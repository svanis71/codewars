import unittest

from kyu4.tcp_states import traverse_TCP_states


class TcpStatesTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]), "CLOSE_WAIT")

    def test_2(self):
        self.assertEqual(traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]), "ESTABLISHED")

    def test_3(self):
        self.assertEqual(traverse_TCP_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]), "LAST_ACK")

    def test_4(self):
        self.assertEqual(traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")

    def test_5(self):
        self.assertEqual(traverse_TCP_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", "APP_SEND"]),
                         "ERROR")


if __name__ == '__main__':
    unittest.main()
