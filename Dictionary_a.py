# Id-20CS102  Name-Janesh Vyas
# Write a Python script to check whether a given key already exists in a dictionary.
new_dict={0:1,1:2,2:3}
def check_key(dict,key):
    if key in dict.keys():
        print('Key is present')
    else:
        print('Key is not present')

check_key(new_dict,1)