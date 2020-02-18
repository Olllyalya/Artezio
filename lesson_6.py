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
