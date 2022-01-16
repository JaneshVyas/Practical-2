# Id-20CS102  Name-Janesh Vyas
# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
new_list=[1,2,1,3,1,4]
total_cnt=0
num=new_list[0]
for i in new_list:
    cnt=new_list.count(i)
    if(cnt>total_cnt):
        total_cnt=cnt
        num=i
print(num,' is most common element it appears',total_cnt, 'times in the list')

new_tuple=(1,2,1,3,3,3,4)
total_cnt=0
for j in new_tuple:
    cnt=new_tuple.count(j)
    if(cnt>total_cnt):
        total_cnt=cnt
        num=j
print(num,' is the most common element it appears',total_cnt,'times in the tuple')

new_dict={0:1,1:1,2:1,3:2,4:3,5:4}
temp={}
for key,value in new_dict.items():
    if value not in temp:
        temp[value]=1
    else:
        temp[value]+=1
max_value=max(temp,key=temp.get)
print(max_value,'is the most common element it appears',temp.get(max_value),'times in the dictionary')