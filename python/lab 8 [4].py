names={"yash","anshul","sam","abhiraj","selvi"}
a_names = {name for name in names if name.startswith("a")}
s_names = {name for name in names if name.startswith("s")}
y_names = {name for name in names if name.startswith("y")}
print("names starting with a:", a_names)
print("names starting with s:", s_names)
print("names starting with y:", y_names)

