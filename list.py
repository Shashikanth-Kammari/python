my_list= ["naresh","suresh","ravi","karthik","shiva"]
print(len(my_list))

#append will add the element at the last 
my_list.append("chary")
print(len(my_list))
print(my_list)

last_element=my_list[len(my_list) -1]
print(last_element)

#extend 

extend_list={10,20,30}
extend_list.add(40)
print(extend_list, len(extend_list))
print(len(extend_list), my_list)