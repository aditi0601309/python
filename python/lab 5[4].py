food_items = [("momos",10),("chicken",5),("pizza",4),("burger",6),("kabab",10)]
sorted_items = sorted(food_items,key = lambda x: x[1], reverse=True)
print("sorted food items by price:",sorted_items)
