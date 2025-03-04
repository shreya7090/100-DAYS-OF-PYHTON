'''
{
key:value,
key2:value2,
value may be [list] or {dict}
}
{
key:[list],
key2:{dict},
}
'''
names = {
   "shreya":"patil",
   "sunita":"lama",
}

#nested list in dict
travel_log = {
    "India":["Goa","karnataka","kashmir","kerala"],
    "Germany":["sugar","water"]
}

#print kashmir
print(travel_log["India"][2])

#nested list
nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

#nesting dict into the dict
travel_log = {
    "India":{
        "total visits":4,
        "cities visited":["Goa","karnataka","kashmir","kerala"]
        },
    "Germany":{
        "total visits":2,
        "cities visited": ["stuttgart","berlin"]
    }
}

print(travel_log["Germany"]["cities visited"][1])

