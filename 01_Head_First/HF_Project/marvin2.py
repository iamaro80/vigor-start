paranoid_android = "Marvin, the paranoid android"
letters = list(paranoid_android)
print(letters)

for char in letters[:6]:
    print('\t',char)
for char in letters[-7:]:
    print('\t'*2,char)
for char in letters[12:20]:
    print('\t'*3,char)
