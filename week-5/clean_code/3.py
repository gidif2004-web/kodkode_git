def validation(new_name, new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True

def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return average, top_count, failing_count

def print_report(stats, names, grades):
    average = stats[0] 
    top_count = stats[1] 
    failing_count = stats[2]
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

def save_to_file(names, grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

def manage_students(names, grades, new_name, new_grade):
    # validation
    if not validation(new_name, new_grade):
        return grades

    # add student
    grades.append(new_grade)
    names.append(new_name)

    # calculate stats
    stats = calculate_stats(grades)

    # print report
    print_report(stats, names, grades)

    # save to file
    save_to_file(names, grades)

    return names, grades