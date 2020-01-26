
1.

def capitalze_frst_ltr(name):
    words = name.split()
    spisok = []
    for word in words:
        new_words = word[:1].upper() + word[1:]
        spisok.append(new_words)
    final_name = (' '.join(spisok))
    print(final_name)


a = input()
capitalze_frst_ltr(a)



2.

def count_caracters(expresion):
    dictionary = {}
    for element in expresion:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    print(dictionary)

expresion = input()
count_caracters(expresion)

3.


def first_and_last_signs(word):
    if len(word) < 2:
        print('Empty String')
    elif len(word) == 2:
        print(word*2)
    else:
        slized_word = word[:2] + word[-2:]
        print(slized_word)

word = input()
first_and_last_signs(word)

4.

list_of_strings = ['abc', 'xyz', 'aba', '1221', 'ekldkf848ek', 'fsef', 's']
print(list_of_strings)
def counter(list_of_strings):
    count = 0
    for element in list_of_strings:
        if (len(element) >= 2 and element[0] == element[-1]):
            count = count +1
    print(count)

counter(list_of_strings)


5.


first_set = set([1,2])
second_set = set([3,4])
third_set = set([5])

def is_it_subset(first_set, second_set, third_set):
    answer = third_set.issubset(first_set) and third_set.issubset(second_set)
    print(answer)

is_it_subset(first_set, second_set, third_set)


6.

n = input()
def create_double_value_dictionary(n):
    n = int(n)
    final_dictionary = {a:a**2 for a in range(1, n+1)}
    print(final_dictionary)

create_double_value_dictionary(n)

7.


dictionary_1 = {1: 'Canada', 2: 'UK', 3: 'Russia'}
dictionary_2 = {1: 'Poland', 3: 'Spain', 4: 'Italy'}
def merge_dictionaries(a, b):
    merged_dict = {**dictionary_1, **dictionary_2}
    print(merged_dict)

merge_dictionaries(dictionary_1, dictionary_2)

8.

from collections import Counter

dictionary_1 = {'Canada': 44, 'UK': 23, 'Russia': 15, 'Poland': 90.2}
def highest_value(dictionary):
    schetchik = Counter(dictionary)
    the_highest = schetchik.most_common(3)
    print(the_highest)

highest_value(dictionary_1)


9.

my_list = [1,2,0,3,4,5,5,6,7,8,8,9,0,0]
def remove_duplicate(a): #порядок элементов не сохраняется
    unic_value_list= set(a)
    print(unic_value_list)

remove_duplicate(my_list)


my_list = [1,2,0,3,4,5,5,6,7,8,8,9,0,0]
def remove_duplicate_2(a): #сохраняется порядок элементов
    unic_value_list = []
    for i in my_list:
        if i not in unic_value_list:
            unic_value_list.append(i)
    print(unic_value_list)

remove_duplicate_2(my_list)


10.

my_first_list = [1,2,3,4,5,5,6,7,8,8,9,0,0]
my_second_list = [2,3,4,5,6,7,8,9,10]
def difference_of_lists(first_list, second_list):
    print(list(set(first_list) - set(second_list)))

difference_of_lists(my_first_list, my_second_list)
