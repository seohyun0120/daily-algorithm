x = input()

check = ["U", "C", "P", "C"]
isChecked = True

for i in range(len(check)):
    if check[i] in x:
        isChecked = True
        idx = x.find(check[i])
        x = x[idx+1:]
    else:
        isChecked = False
        break

if isChecked == True:
    print("I love UCPC")
else:
    print("I hate UCPC")
