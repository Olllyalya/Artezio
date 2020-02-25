class EvenIterator(object):

    def __int__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(1, len(my_list)+1, 2):
            print(i)
        else:
            raise StopIteration

            
            
            
 list_generat = [arg for arg in dir(Foo) if not arg.startswith('_')]




from itertools import zip_longest

list_1 = [1,2,3]
list_2 = ['a','b','c','d']

final_dist = {k: v for k, v in zip_longest(list_1, list_2) if k is not None}
