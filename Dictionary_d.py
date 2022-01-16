# Id-20CS102  Name-Janesh Vyas
# Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
new_dict={0:10,1:20}
print('Sample Dictionary:',new_dict)
new_dict.update({2:30})
print('Expected Reasult:',new_dict)