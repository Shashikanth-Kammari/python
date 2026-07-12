my_list= ["naresh","suresh","ravi","karthik","shiva"]
print(my_list)

#append will add the element at the last 
my_list.append(my_list)
print(len(my_list))

last_element=my_list[len(my_list) -1]
print(last_element)

#extend 

extend_list=[10,20,30]
extend_list.extend(extend_list)
print(len(extend_list), extend_list)