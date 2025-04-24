student=[("anshul","sam"),"selvi","priyanshi",("umang","yash"),"anoushka","aditi"]
boys_count=sum(1 for ele in student if isinstance(ele, tuple))
girls_count=len(student) - boys_count
print("number of boys:",boys_count)
print("number of girls:",girls_count)
