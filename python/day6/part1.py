with open("data.txt", "r") as p:
    lines=p.readlines()

groups = []
group = []
for question in lines:
    if question!="\n":
        group.append(question.split("\n")[0])
    else:
        groups.append(group)
        group=[]
groups.append(group)



solution_1 = []
for group in groups:
    print(f"Group: ", group)
    unique_ques = []
    for ques in group:
        unique_ques.extend([uq for uq in ques])

    print(f"Unique questions: {set(unique_ques)}")
    solution_1.extend(list(set(unique_ques)))
print(f"p1: {len(solution_1)}")