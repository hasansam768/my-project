#variables
age=22 #in python age is the variable's location. it doesn't have a fixed size. we can assign any value in any size any data type.
name="samha"
firstName="x"
first_name="x"
_first_name="x" #can use _ anywhere.
first12name4="x" #can't use no in the beginning of the variable name.


#################################################################################################################################


#str or string
brand='samsung12%'
print(type(brand)) #output <class 'str'>
print(brand[0])    #in python string is cosidered as an array
#print(brand[15])   #output: error:index is out of range
paragraph='''nsdhncjhbhb''' #multiple line str can be written in double or single quotation
print(len(brand))   #output: 10

#list
places=["ad","tyu",25,54]
print=(places[0])

#tuple
places=("ad","tyu",25,54)

#set
places={"ad","tyu",25,54}

#dictionary or dict
details={"name":"sam", "age":22}

#bool
name="sam"
_is_student=True #in python true's first letter must be capital
#print(type(_is_student))  #output <class 'bool'>

#slicing 
brand='samsung12%'
print(brand[1:4]) #ams (1 to 3)
print(brand[1:])  #amsung12%
print(brand[:4])  #sams
print(brand[:])   #samsung12%  (no need)
print(brand[-1])  #%

#concatination
first_name="ab"
last_name="cd"
full_name=first_name + last_name   #abcd
full_name=first_name + " " + last_name #ab cd

#formatting   
print (f"my name is {first_name} {last_name}")    #my name is ab cd

#escape characters
print("my name is \"ab cd\"" ) #my name is "ab cd"

text="I have banana, apple"
#if you type . after variable name the menu shows so many options. that can be done for string
print(text.upper) #"I HAVE BANANA, APPLE"
print(text.strip) #remove first and last space in text
print(text.split("")) #["I", "have", "banana", "apple"]
print(text.replace("i have", "fruit")) #fruit banana, apple
print(text.split(",")) #["I have banana", "apple"]

fruit="banana, apple, mango"
print(text.split(","))  #["banana", " apple", " mango"]
#using split we can convert text to list

