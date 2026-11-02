# i=0;
# while i<=10:
#     print(i);
#     i+=1;
#prctice 1 while loop
# prints number from 1 to 100;
# i=1;
# while i<=100:
#     print(i);
#     i+=1;
# pract 2 
# print number from 100 to 1;
# i=100;
# while i>=1:
#     print(i);
#     i-=1;

# pract 3
# print the multiplication table of a number n 
# i=1;
# while i<=10:
#     print(5*i);
#     i+=1;
   
# 4
# print the elements of the following list using a loof
nums=[1,4,9,16,25,36,49,64,81,100];
# heros =["spiderman","ironman","thor","hulk","captain america"];
# idx2=0;
# while idx2<len(heros):
#     print(heros[idx2]);
#     idx2+=1;

# idx=0;
# while idx<len(nums):
#     print(nums[idx]);
#     idx+=1;


# 5 
# search for a number x in the tuple using loop
tup=(1,2,3,4,5,6,7,8,9,10);

# tup=(1,2,3,4,5,6,7,8,9,10);
# i=0;
# while i<len(tup):
#     if tup[i]==5:
#         print("found",i);
#         break;
#     i+=1;
# i=1;
# while i<=5:
#     print(i);
#     if i==3:
#         break;
#     i+=1;
# i=1;
# while i<=5:
   
#     if (i==3):
#         i+=1;
#         continue;
#     print(i);
#     i+=1;



# for
# veggies=["potato","tomato","onion","carrot"];
# for veggie in veggies:
#     if (veggie=='tomato'):
#         print("tomato is  available");
#         break;
        
    
#     print(veggie);
# else:
#     print("no more veggies left");

# for i in range(10):
#     print(i);
# print("hello");
# for i in range(1,10):
#     print(i);
# print("hellweo");

# for i in range(0,10,5):
#     print(i);

# for i in range(2,11,2):
#     print(i,"even");


# pract 1
#  print number s form 1 to 100 using for loop
# for i in range(1,101):
#     print(i);

# pract 2
# print number from 100 to 1 using for loop
# for i in range(100,0,-1):
#     print(i);

# for i in range(1,11):
#     print(" 5 * ",i," = ",5*i);


# for i in range(5):
#     pass
# print("rafi")    


# n=5;
# sum=0;
# for i in range(n+1):
#     sum+=i
# print(sum)


n=5;
fact=1;

for i in range(1,n+1):
    fact*=i;
print("Factorial of", n, "is", fact);