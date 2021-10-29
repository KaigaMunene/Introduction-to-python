# 5.Write a Python program to remove duplicates from a list.

# def remove_duplicates(my_list):
#     return set(my_list)
# print(remove_duplicates(["a","b","c","a","d","c","e"]))

# def remove_duplicates(my_list):
#     return list(dict.fromkeys(my_list))
# print(remove_duplicates(["a","b","c","a","d","c","e"]))

def convert_list_to_dict(mylist):
    mydict={}
    for i in mylist:
        mydict[i]= None
    return mydict
print(convert_list_to_dict(["a","b","c","a","d","c","e"]))