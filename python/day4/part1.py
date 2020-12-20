from data import data
	
split_input = data.split("\n\n")

split_input_2 = [string.replace("\n", " ") for string in split_input]

split_input_3 = [string.split() for string in split_input_2]

def convert_to_dictionary(password_list):
    dictionary = {}
    for item in password_list:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        dictionary[key] = value
    return dictionary
passports = [convert_to_dictionary(item) for item in split_input_3]


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
def is_valid_passport(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    # has_country_id = "cid" in passport
    
    return (
        has_birth_year and
        has_issue_year and
        has_expiration_year and
        has_height and
        has_hair_color and
        has_eye_color and
        has_passport_id
    )

print(len([passport for passport in passports if is_valid_passport(passport)]))