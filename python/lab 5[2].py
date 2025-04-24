student=[(33,"Aditi",18),(35,"Anshul",19),(56,"sam",19),(111,"selvi",18),(146,"yash",20)]
roll_no,names,ages=zip(*student)
print("Roll numbers:", list(roll_no))
print("names:", list(names))
print("Ages:", list(ages))
