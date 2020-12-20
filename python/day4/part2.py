from part1 import passports, is_valid_passport


def has_valid_values(passport):
    has_valid_birth_year = 1920 <= int(passport["byr"]) <= 2002
    has_valid_issue_year = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_expiration_year = 2020 <= int(passport["eyr"]) <= 2030
    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76
    def is_valid_hex_string(string):
        is_valid = True
        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break
        return is_valid    
    has_valid_hair_color = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hair_color = is_valid_hex_string(digits)
    has_valid_eye_color = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    def is_valid_passport_id(value):
        is_valid = False
        if len(value) == 9:
            is_valid = True
            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break
        return is_valid
    has_valid_passport_id = is_valid_passport_id(passport["pid"])
    return (
        has_valid_birth_year and
        has_valid_issue_year and
        has_valid_expiration_year and
        has_valid_height and
        has_valid_hair_color and
        has_valid_eye_color and
        has_valid_passport_id
    )
    

truly_valid_passports = [passport for passport in [passport for passport in passports if is_valid_passport(passport)] if has_valid_values(passport)]
print(len(truly_valid_passports))