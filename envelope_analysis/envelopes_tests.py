import unittest
import sys
import subprocess

from envelope_2 import Envelope


class TestClassEnvelopeAnalysis(unittest.TestCase):

    def test_wrong_side_type_error(self):
        # Assert for exception
        self.assertRaises(TypeError, lambda: Envelope("str", True))
        self.assertRaises(TypeError, lambda: Envelope(9, "abc"))
        self.assertRaises(TypeError, lambda: Envelope(True, 5))
        self.assertRaises(TypeError, lambda: Envelope(False, 7.1))
        self.assertRaises(TypeError, lambda: Envelope(5, True))
        self.assertRaises(TypeError, lambda: Envelope(9.3, "bc"))
        self.assertRaises(TypeError, lambda: Envelope("qbc", 9.9))
        self.assertRaises(TypeError, lambda: Envelope(7, 8.1))
        self.assertRaises(TypeError, lambda: Envelope(5.0, 6))
        self.assertRaises(TypeError, lambda: Envelope(5, 5.0))

    def test_incorrect_value_sides_error(self):
        self.assertRaises(ValueError, lambda: Envelope(7.2, -2.9))
        self.assertRaises(ValueError, lambda: Envelope(-7.5, 6.2))
        self.assertRaises(ValueError, lambda: Envelope(-8.4, -8.3))

    def test_is_envelope_bigger(self):
        envelope_obj_1 = Envelope(5.1, 1.2)
        envelope_obj_2 = Envelope(8.3, 6.7)
        envelope_obj_3 = Envelope(5.3, 10.0)
        envelope_obj_4 = Envelope(10.0, 5.1)

        self.assertFalse(envelope_obj_1.is_envelope_bigger(envelope_obj_2))
        self.assertTrue(envelope_obj_2.is_envelope_bigger(envelope_obj_1))
        self.assertFalse(envelope_obj_3.is_envelope_bigger(envelope_obj_2))
        self.assertTrue(envelope_obj_4.is_envelope_bigger(envelope_obj_1))
        self.assertTrue(envelope_obj_2.is_envelope_bigger(envelope_obj_1))


if __name__ == '__main__':
    unittest.main()
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
