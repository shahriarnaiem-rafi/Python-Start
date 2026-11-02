# # dictationary
# student={
#     "name":"Rafi",
#     "age":23,
#     "university":"BUBT",
#     "subject":["english","math","cse"],

# }
# # show the dictationary
# print(student);

# #find value with key 
# print(student["age"]);
# print(student["subject"][0]);
# # find all keys
# print(student.keys());
# # find all values
# print(student.values());



# nul_dic={

# }
# nul_dic["name"]="Rafi";
# nul_dic["age"]=23;
# print(nul_dic);

# nasted dic

student={
    "name":"Rafi",
    "age":23,
    "university":"BUBT",
    "subject":{
        "math":90,
        "english":85,
        "bangla":88
        },

}
# print(student["subject"]["math"]);
# # print(list(student.keys()));
# # touple akare ase
# print(student.items());
# # print(list(student.items()));
# # print(student.get("age"));
# student.update({"age":20});
# print(student);


# set
# uniq and ummutable

# my_set = {1, 3,2, 3.3, 4, 5}
# print(my_set)
# nul_set = set()
# print(nul_set)
# my_set.add(10)
# my_set.remove(2)
# print(my_set)
# my_set.pop();
# print(my_set)
# my_set.clear();
# print(my_set)
# my_set2 = {1, 2, 3, 4, 9,95}
# # print(my_set2)
# # uniq value show korbe 

# my_set.union(my_set2);
# # print(my_set)

# inter=my_set.intersection(my_set2);
# print(inter)

# set1={1, 2, 3, 4, 5}
# set2={4, 5, 6, 7, 8}
# # common value show korbe
# set1.intersection_update(set2)
# print(set1)

#1 practice ques 

# dictionary={
#     "cat":"a small animal",
#     "table":["a piece of furniture","a list of facts & figures"]
# }
# print(dictionary)



# 2 practice

# set1={"python","java","c++","python","java","javascript","python","java","c++","c"}
# print(len(set1))



# 3 practice
# marks={};
# x=int(input("Enter the number of physics: "));
# marks.update({"Physics":x});
# y=int(input("Enter the number of math: "));
# marks.update({"Math":y});
# z=int(input("Enter the number of chemistry: "));
# marks.update({"Chemistry":z});
# print(marks);

# 4 practice

values={9,"9.0"};#possible to add string and int in set
# built-in function
values2={
    ("float",9.0),
    ("int",9),
}
print(values);
print(values2);
