#Create an empty list
services_list = []

#Populate the list using append
services_list.append('EC2')  
services_list.append("S3")
services_list.append("Lambda")                                                                                                       
services_list.append("Dynamo DB")  

#Print the list and the length of the list
print(services_list)
print(len(services_list))

#Remove two specific services from the list by name or by index
del services_list[1:3]

#Print the new list and the new length of the list
print(services_list)
print(len(services_list))