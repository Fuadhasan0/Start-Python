# Bangladesh division info
bd_info ={
       "Barishal": {"District": 6, "Upazila": 39, "Union": 333},
       "Chittagong": {"District": 11, "Upazila": 97, "Union": 336},
       "Dhaka": {"District": 13, "Upazila": 93, "Union": 1833},
       "Khulna": {"District": 10, "Upazila": 59, "Union": 270},
       "Mymansingh": {"District": 4, "Upazila": 34, "Union": 350},
       "Rajshahi": {"District": 8, "Upazila": 70, "Union": 558},
       "Sylhet": {"District": 4, "Upazila": 38, "Union": 334},
       "Rangpur": {"District": 8, "Upazila": 58, "Union": 536}
}

# Print bd_info DICTIONARY
print("bd_info DICTONARY\n~",bd_info)

# Print bd_info with loop
print("bd_info print with loop\n~")

for x in bd_info:
       print(bd_info[x],"\n")
       
# Print key with loop
print("Key print with loop\n~")

for item in bd_info:
       print( item) 
       
# Print key with key function
print("Key print with key function\n~")

divisions = bd_info.keys()
print(divisions)

# Print key with loop and key function
print("Key pritn with loop and key function\n~")

for division in divisions:
       print("Division", division)  
       
# Print Division and Upzila with loop
print("Key and 1 value\n~")

for division in divisions:
       print(division,"\t", "District:", bd_info[division]["District"], "\t", "Upazila:", bd_info[division]["Upazila"], "\t", "Union:", bd_info[division]["Union"], "\n") 
       
# Print key and value with loop
print("Key and value\n~")

for key in bd_info:
       print(key)
       print(bd_info[key])       
       