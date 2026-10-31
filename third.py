# array    is called lists
# marks1=94.42
# marks2=94.43
# marks3=94.3

# marks=[23,44,65,78,"45"];


# print(type(marks))
# print(len(marks))
# print(marks)
# print(marks[1])
# print(type(marks[4]))

# student =["rafi",23,34,"dhaka"]
# student[0]="naiem"
# print(student[3])

# print(student)

# sublist 
marks=[23,44,65,78,"45"];
# print(marks[1:4])
# print(marks[4:])

# # neg
# print(marks[-3:-1])
# # list method

# marks.append(4);
# print(marks);
num=[2,4,1,5,7,2]
# # 1234567
# num.sort();
# print(num)



# num.sort(reverse=True);
# print(num)

# num.reverse();

# print(num)

# num.insert(4,100)
# print(num)


# # remove methon
# num.remove(2)
# print(num)



# num.pop(1)
# print(num)
# print(num.count(2))




# tupple

# immutable sequence  not for change

# tup=(2,3,4,5)
# print(tup[0])
# print(type(tup))
# index a giye value change kora jabe na
# tup1=(1,3,4,5,6,3)
# # print(type(tup1))




# # print(tup1[1:3])
# # print(tup1.index(3))
# # print(tup1.count(3))


# # practice 1
# movies=[];
# movie1=input("enter first name")
# movie2=input("enter first name")
# movie3=input("enter first name")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)


# favouritemovies=[input("enter a list ")]
# print(favouritemovies)

# practice 2

# check if a list contains a palindrome of elements hint use copy method

lis1=[1,2,3,2,1,2];
lis2=[1,2,3]
copy_lis1=lis1.copy();
copy_lis1.reverse();
if(lis1 == copy_lis1):
    print("palindrome")
else:
    print("not palindrome")


# practce 3

grade=("c","d","a", "a","d");
print(grade.count("a"))

# prac 4


grade2=["c","d","a", "a","d"];
grade2.sort();
print(grade2)

