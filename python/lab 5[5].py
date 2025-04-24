tuples_list=[(),(1,2,3),(),(4,5),()<("hello",)]
filterd_list = [tup for tup in tuples_list if tup]
print("list after removing empty tuple:",filterd_list)
