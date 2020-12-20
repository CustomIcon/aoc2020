from part1 import convert_to_pass_policy_dic, data_split


def meets_new_password_policy(pass_n_policy):
    first_position = pass_n_policy["min"]
    char_in_first_position = (
        pass_n_policy["password"][first_position - 1] == pass_n_policy["char"]
    )
    second_position = pass_n_policy["max"]
    char_in_second_position = (
        pass_n_policy["password"][second_position - 1] == pass_n_policy["char"]
    )
    return char_in_first_position ^ char_in_second_position


print(
    len(
        list(
            filter(
                meets_new_password_policy,
                [
                    convert_to_pass_policy_dic(password_and_policy)
                    for password_and_policy in data_split
                ],
            )
        )
    )
)
