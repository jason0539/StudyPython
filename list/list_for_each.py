movies = ["one","two",["one","two",["one","two","three"]]]

print(movies)

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)