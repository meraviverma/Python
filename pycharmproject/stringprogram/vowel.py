# Count and display vowels in a string
# In this program, we need to count the number of vowels present in a string and display those vowels.

# In a simple way
# Input : Geeks for Geeks
# Output :
# 5
# ['e', 'e', 'o', 'e', 'e']
#
# This is in a different way
# Input : Geeks for Geeks
# Output : {'u': 0, 'o': 1, 'e': 4, 'a': 0, 'i': 0}

#Approach 1
str="He is a good boy"
str1="Geeks for Geeks"
vowellist=['a','e','i','o','u']
vowelstr=[]
sum=0
for w in str1:
    if(w in vowellist):
        sum=sum+1
        vowelstr.append(w)
print(sum)
print(vowelstr)

print("########### Approach2 ##########")
#Approach2
#Using dictionary
vowelstr={'a':0,'e':0,'i':0,'o':0,'u':0}
for w in str1:
    if(w in vowellist):
        vowelstr[w]+=1
print(vowelstr)


