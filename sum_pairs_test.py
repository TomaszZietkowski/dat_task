from sum_pairs import SumPairs
import pytest

list_of_numbers = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
data_to_test = [
                (list_of_numbers, -1, []),
                (list_of_numbers, 0, [[0, 0]]),
                (list_of_numbers, 25, []),
                (list_of_numbers, 12, [[0, 12], [0, 12], [1, 11], [4, 8], [4, 8]]),
                (list_of_numbers, 10, [[2, 8], [1, 9]])
                ]

class TestSumPairs():  

    @pytest.mark.parametrize("list_of_numbers, sum_num, list_of_par", data_to_test)
    def test_create_a_pair_list(self, list_of_numbers, sum_num, list_of_par):
        assert SumPairs().create_a_pair_list(list_of_numbers, sum_num) == list_of_par