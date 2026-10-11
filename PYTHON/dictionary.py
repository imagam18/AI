thiss_dic = {
    "brand":"ford",
    "model":"Mustang",
    "year":1986,
    "year":2020,
    "colors":['Red',"blue"]
}
print(thiss_dic)

thisdict = dict(name = "John", age = 36, country = "Norway")
#acessing the items

print(thiss_dic["brand"])
print(thiss_dic["year"])
print(len(thiss_dic))
print(thiss_dic["colors"][1])
print(thisdict)

x = thiss_dic.get("year")
print(x)

x = thiss_dic.keys()
print(x)

thiss_dic['year'] = 2030
print(thiss_dic)


x = thiss_dic.items()
print(x)

if "year" in thiss_dic:
    thiss_dic["year"] = 2050
    print(thiss_dic)
else:
    print(thiss_dic)
    
# thiss_dic.popitem()
# print(thiss_dic)

# loops

for x in thiss_dic:
    print(thiss_dic[x])
    
for x in thiss_dic.values():
    print(x)
    
for x , y in thiss_dic.items():
    print(x,y)
    
my_dic = thiss_dic.copy()
print(my_dic)


# NEsted list 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
print("next")
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
    
u =thiss_dic.get('color', "Vale cant in thatṇ")
print(u)