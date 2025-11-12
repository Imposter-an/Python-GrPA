def courses_sorted_by_enrollment(student_courses: dict) -> list:
    '''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.
    Assume no courses will have the same number of students enrolled.
    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose
    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
    '''
    # Dictionary to count enrollments for each course
    course_count = {}
    
    # Count enrollments for each course
    for student, courses in student_courses.items():
        for course in courses:
            course_count[course] = course_count.get(course, 0) + 1
    
    # Sort courses by enrollment count in descending order
    sorted_courses = sorted(course_count.keys(), key=lambda course: course_count[course], reverse=True)
    
    return sorted_courses