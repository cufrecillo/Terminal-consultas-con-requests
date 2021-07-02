list_of_elements= [1,2,3,4]

for element in list_of_elements:
    print(element)

print([element for element in list_of_elements])

print(map(lambda element: element, list_of_elements))