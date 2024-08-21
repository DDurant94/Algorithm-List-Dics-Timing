import timeit
import time
import sys

def squaring_numbers(amount_of_numbers):
  start_time = time.time()
  squared_numbers = [i**2 for i in range(1,amount_of_numbers+1)]
  end_time = time.time()
  total_time = end_time - start_time
  print(squared_numbers)
  size = sys.getsizeof(squared_numbers)
  print(f'size of my list is {size} bytes')
  print(f'Total run time is: {total_time:.7f}')
  return squared_numbers

code_test = "[i**2 for i in range(1,1000)]"
elapsed_time = timeit.timeit(code_test,number = 1000)
print(f"test of squared_numbers {elapsed_time}")
squaring_numbers(10)


def reversing_sublist(list, i, j):
  start_time = time.time()
  if i < 0 or j >= len(list) or i > j:
    return ValueError("Invalid input")
  
  while i < j:
    list[i], list[j] = list[j],list[i]
    i += 1
    j -= 1
  end_time = time.time()
  total_time = end_time - start_time
  print(f'\nTotal run time is: {total_time:.12f}')
  size = sys.getsizeof(list)
  print(f'size of my reversing_sublist is {size} bytes')
  return list

list =[i for i in range(1,21)]
print(reversing_sublist(list,2,17))

def merging_sorted_lists(list1,list2):
  start_time = time.time()
  merged_list = []
  i,j = 0,0
  
  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i += 1
    else:
      merged_list.append(list2[j])
      j += 1
  
  while i < len(list1):
    merged_list.append(list1[i])
    i += 1
    
  while j < len(list2):
    merged_list.append(list2[j])
    j += 1
  
  end_time = time.time()
  total_time = end_time - start_time
  print(f'\nTotal run time is: {total_time:.12f}')
  size = sys.getsizeof(merged_list)
  print(f'size of my merging_sorted_list is {size} bytes')
  return merged_list

list1=[i for i in range(1,33,3)]
list2 = [i for i in range(3,28,2)]
print(merging_sorted_lists(list1,list2))