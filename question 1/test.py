import unittest
from Overlap import overlap_computer


class OverLapComputerTest(unittest.TestCase):

    def test_all_postive_number_with_overlap(self):
        result = overlap_computer([2, 7], [2, 4])

        self.assertEqual(result, 'THERE IS AN OVERLAP')

    def test_all_postive_number_with_no_overlap(self):
        result = overlap_computer([2, 3], [4, 20])
        self.assertEqual(result, "THERE IS NO OVERLAP")

    def test_mixed_numbers_with_overlap(self):
        result = overlap_computer([-2, 1], [0, -5])
        self.assertEqual(result, 'THERE IS AN OVERLAP')

    def test_mixed_numbers_with_no_overlap(self):
        result = overlap_computer([-2, -6], [5, 9])
        self.assertEqual(result, "THERE IS NO OVERLAP")

    def test_all_negavtive_number_with_overlap(self):
        result = overlap_computer([-7, -10], [-8, -12])
        self.assertEqual(result, 'THERE IS AN OVERLAP')

    def test_all_negavtive_number_with_no_overlap(self):
        result = overlap_computer([-1, -5], [-6, -11])
        self.assertEqual(result, "THERE IS NO OVERLAP")




unittest.main()