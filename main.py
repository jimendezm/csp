from cps_backtracking.csp import initialize, backtracking


# variables <- list of courses
# domain <- list of possible days
# constraints <- list of incompatibilities
variables = ["A", "B", "C"]
domain = ["Monday", "Tuesday"]
constraints = ["A!=B", "C!=A"]


def main():
    courses = initialize(variables, domain)

    first_course = courses[0]
    remaining_courses = courses[1:]
    assigned_courses = []

    if backtracking(first_course, remaining_courses, assigned_courses, constraints):
        for course in courses:
            print(course.name, "->", course.value)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
# run main
