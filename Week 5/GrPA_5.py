def groupby(data: list, key: callable):
    '''
    Group items by a key function.
    '''
    result = {}
    for item in data:
        k = key(item)
        if k not in result:
            result[k] = []
        result[k].append(item)
    return result

def apply_to_groups(groups: dict, func: callable):
    '''
    Apply a function to the list of items for each group.
    '''
    return dict(map(lambda kv: (kv[0], func(kv[1])), groups.items()))

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    it = map(lambda s: s[course], student_data)
    return min(it)

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    it = map(lambda s: s[course], student_data)
    return max(it)

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    return max(student_data, key=lambda s: s[course])["rollno"]

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks.
    '''
    sorted_students = sorted(student_data, key=lambda s: (s[course1], s[course2], s[course3]))
    return list(map(lambda s: s["rollno"], sorted_students))

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    return apply_to_groups(groupby(student_data, lambda s: s["city"]), len)

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    counts = count_students_by_cities(student_data)
    return max(counts.items(), key=lambda x: x[1])[0]

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and a sorted list of rollno of students that belong to that city as the value.
    '''
    groups = groupby(student_data, lambda s: s["city"])
    return dict(
        map(lambda kv: (kv[0], sorted(map(lambda s: s["rollno"], kv[1]))), groups.items())
    )

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    groups = groupby(student_data, lambda s: s["city"])
    avg_per_city = dict(
        map(
            lambda kv: (kv[0], sum(map(lambda s: s[course], kv[1])) / len(kv[1])),
            groups.items()
        )
    )
    return max(avg_per_city.items(), key=lambda x: x[1])[0]