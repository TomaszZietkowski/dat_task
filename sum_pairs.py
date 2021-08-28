'''Pairs of numbers whose sum is specified'''
from os import cpu_count
from typing import List
import copy


class SumPairs():
    '''
    A class with pairs of numbers whose sum is specified
    ...
    Attribute
    ----------
    list_of_numbers : List(int)
        List of numbers from
         which pairs will be found
    sum_num : int
        A number that represents the sum of the pair
    Methods
    -------
    run_app()
        Launches applications
    create_a_pair_list(list_of_numbers, sum_num)
        Lists the pairs whose sum is sum_num
    __check_component_is_in_the_list(list_of_numbers, component_b)
        Checks if the number is in the list
    read_data_from_file()
        Loading data from a file
    save_data_to_file()
        Save data to a file
    '''

    def __init__(self) -> None:
        '''
        Constructs all the necessary attributes for the object.

        Parameters
        ----------
            list_of_numbers: List(int)
                List of numbers from which pairs will be found
            list_of_par: List(int)
                List with pairs of numbers
            sum_num : int
                A number that represents the sum of the pair

        '''
        self.list_of_numbers = []
        self.list_of_par = []
        self.sum_num = 0

    def run_app(self) -> None:
        '''Launches application'''

        self.read_data_from_file()
        self.list_of_par = self.create_a_pair_list(self.list_of_numbers, self.sum_num)
        self.save_data_to_file()

    def create_a_pair_list(self, list_of_numbers:List, sum_num:int) -> List:
        '''
        Create the pairs whose sum is sum_num

        Parameters
        ----------
        list_of_numbers: List(int)
                List of numbers from which pairs will be found
        sum_num : int
                A number that represents the sum of the pair

        Returns
        -------
        list_of_par: List(int)
                List with par of numbers
        '''
        copy_list_of_numbers = copy.deepcopy(list_of_numbers)
        list_of_par = []
        print('Create the pairs')
        while copy_list_of_numbers != []:
            component_a = copy_list_of_numbers.pop()
            component_b = sum_num - component_a
            if self.__check_component_is_in_the_list(copy_list_of_numbers, component_b):
                list_of_par.append(sorted([component_a, component_b]))
                copy_list_of_numbers.remove(component_b)
        return list_of_par

    @staticmethod
    def __check_component_is_in_the_list(list_of_numbers:List, component_b:int) -> bool:
        '''
        Checks if the number is in the list

        Parameters
        ----------
        list_of_numbers: List(int)
            List of numbers from which pairs will be found
        component_b : int
            Number to check

        Returns
        -------
        bool
        '''
        try:
            return list_of_numbers.index(component_b) != -1
        except ValueError:
            return False

    def read_data_from_file(self) -> None:
        '''
        Read data from file data_to_read.txt

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        with open('data_to_read.txt', 'r') as file:
            print('Read data from file')
            self.list_of_numbers = list(map(int, file.readline().split(',')))
            self.sum_num = int(file.readline())

    def save_data_to_file(self) -> None:
        '''
        Save data to file save_data.txt

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        with open('save_data.txt', 'w') as file:
            print('Save data to file')
            file.write(str(self.list_of_par))

if __name__ == '__main__':
    SumPairs().run_app()
