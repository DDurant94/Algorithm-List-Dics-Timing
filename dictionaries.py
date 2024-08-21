import time
import sys
start_time = time.time()
end_time = time.time()
total_time = end_time - start_time
print(f'Total run time is: {total_time:.7f}')


def merging_dics(dict1,dict2):
  start_time = time.time()
  merged_dict = dict1.copy()
  merged_dict.update(dict2)
  end_time = time.time()
  size = sys.getsizeof(merged_dict)
  total_time = end_time - start_time
  print(f'Total run time is: {total_time:.7f}')
  print(f'size of my list is {size} bytes')
  return merged_dict


dict1 = {"John Doe": "john_doe@example.com"}
dict2 = {"Jane Doe": "jane_doe@example.com"}
print(merging_dics(dict1,dict2))


def intersect_dicts(dict1,dict2):
  start_time = time.time()
  intersect = {i:(f'dict one: "{dict1[i]}"', f'dict two: "{dict2[i]}"') for i in dict1 if i in dict2}
  end_time = time.time()
  size = sys.getsizeof(intersect)
  total_time = end_time - start_time
  print(f'Total run time is: {total_time:.7f}')
  print(f'size of my list is {size} bytes')
  return intersect

dict11 = {'a':1,'b':2,'c':3}
dict22 = {'b':'a','c':'b','d':'c'}

print(intersect_dicts(dict11,dict22))


def unique_word_finder(list):
  start_time = time.time()
  unique_word_count = {}
  for word in list:
    if word in unique_word_count:
      unique_word_count[word] +=1
    else:
      unique_word_count[word] = 1
  end_time = time.time()
  size = sys.getsizeof(unique_word_count)
  total_time = end_time - start_time
  print(f'Total run time is: {total_time:.7f}')
  print(f'size of my list is {size} bytes')
  return unique_word_count  


word_list = ['hello','coding', 'temple', 'code', 'hello', 'temple', 'temple']

print(unique_word_finder(word_list))