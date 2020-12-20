from data import data

data_split = data.split("\n")


def convert_to_pass_policy_dic(line):
    pass_policy_dic = {}
    pass_n_policy_list = line.split()
    min_max = pass_n_policy_list[0].split("-")
    pass_policy_dic["min"] = int(min_max[0])
    pass_policy_dic["max"] = int(min_max[1])
    pass_policy_dic["char"] = pass_n_policy_list[1][0]
    pass_policy_dic["password"] = pass_n_policy_list[2]
    return pass_policy_dic


def meets_password_policy(pass_n_policy):
    char_count_in_password = pass_n_policy["password"].count(pass_n_policy["char"])
    return pass_n_policy["min"] <= char_count_in_password <= pass_n_policy["max"]


print(
    len(
        list(
            filter(
                meets_password_policy,
                [
                    convert_to_pass_policy_dic(pass_n_policy)
                    for pass_n_policy in data_split
                ],
            )
        )
    )
)
