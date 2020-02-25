1.
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

            
            
            
 2.
list_generat = [arg for arg in dir(Foo) if not arg.startswith('_')]




3.
from itertools import zip_longest

list_1 = [1,2,3]
list_2 = ['a','b','c','d']

final_dist = {k: v for k, v in zip_longest(list_1, list_2) if k is not None}


4.
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
                
                
5.
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
