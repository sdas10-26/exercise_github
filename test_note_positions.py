import unittest
from note_positions import get_fret, get_frets

class TestFindFret(unittest.TestCase):
    def test_same_note(self):
        """Test whether passing in the same value for target and string gives a return value of 0."""
        self.assertEqual(get_fret("C", "C"), 0)
        self.assertEqual(get_fret("G#", "G#"), 0)

    def test_target_higher_than_string(self):
        """Test at least one case where target corresponds to a larger number in your dictionary than string."""
        self.assertEqual(get_fret("A", "C"), 9)
        self.assertEqual(get_fret("D", "B"), 3)

    def test_target_lower_than_string(self):
        """Test at least one case where target corresponds to a smaller number in your dictionary than string."""
        self.assertEqual(get_fret("C", "A"), 3)
        self.assertEqual(get_fret("F", "G"), 10)

    def test_sharp_equals_flat(self):
        """Test whether the function returns the same value when target is the sharp as when target is the flat."""
        self.assertEqual(get_fret("G#", "C"), get_fret("Ab", "C"))
        self.assertEqual(get_fret("D#", "G"), get_fret("Eb", "G"))

    def test_get_frets_single_string(self):
        """Test the function with a list consisting of a single string."""
        self.assertEqual(get_frets("B", ["G"]), {"G": 4})

    def test_get_frets_multiple_strings(self):
        """Test the function with a list consisting of multiple strings of different values."""
        expected_result = {"G": 4, "C": 11, "E": 7, "A": 2}
        self.assertEqual(get_frets("B", ["G", "C", "E", "A"]), expected_result)

if __name__ == "__main__":
    unittest.main()
