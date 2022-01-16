# Id-20CS102  Name-Janesh Vyas
# Write a Python program to sum all the items in a dictionary.
new_dict={0:100,2:300,5:100}
def total_sum(dict):
    sum=0
    for i in dict.values():
        sum=sum+i
        
    print(sum)

total_sum(new_dict)