string = raw_input()

iter_string = list(string)
uniqs = list(set(iter_string))
count_list = []

for ele in uniqs:
	ya = iter_string.count(ele)%2
	print ya
	if ya!= None:
		count_list.append(ya)  
                 
                   
                      
found = False if sum(count_list)>1 else True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not found:
    print("NO")
else:
    print("YES")