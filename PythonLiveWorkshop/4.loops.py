## How to store data in python?
##list =>data structure which can hold multiple values of multi types
## arrays=> data structure which can hold multiple values of same types
list_of_cloud = [
    "aws",
    "oracle",
    "gcp",
    "azure",
    "digital ocean",
    "cloud ways",
    "alibaba",
]
print(list_of_cloud)
## add new cloud
list_of_cloud.append("oci")
## add one more cloud
list_of_cloud.append("IBM")  # append is used to add in the end of list
print(list_of_cloud)
## insert in between list any item
list_of_cloud.insert(3, "a cloud")
print(list_of_cloud)
## length of element of list
print(len(list_of_cloud))
## list index starts  from 0, 1, 2, 3 .....
list_of_cloud.insert(0, "Hello cloud:")
print(list_of_cloud)
### loops used to iterate in columns of lists
## Iteration of list
for cloud in list_of_cloud:
    print(" ")  # Whwn 4 spaces from left =>identation
    print(cloud)  # Output in column
for i in range(0, 10):
    print(i)
for i in range(1, 11):
    print(i)
for i in range(1, 11):
    print("Welcome to coding")  # output welcome to codimg*10
