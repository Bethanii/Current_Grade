name = input("Please enter your name: ")
course = input("Please enter your course name: ")


def current_grade():
    quizzes_weight = float(input("Enter quizzes weight: "))
    projects_weight = float(input("Enter projects weight: "))
    activities_weight = float(input("Enter activities weight: "))
    attendance_weight = float(input("Enter attendance weight: "))
    exams_weight = float(input("Enter exams weight: "))

    quizzes_average = float(input("Enter quizzes average: "))
    projects_average = float(input("Enter projects average: "))
    activities_average = float(input("Enter activities average: "))
    attendance_average = float(input("Enter attendance average: "))
    exams_average = float(input("Enter exams average: "))

    grade = str(quizzes_weight/100*quizzes_average + projects_weight/100*projects_average + activities_weight/100*activities_average + attendance_weight/100*attendance_average + exams_weight/100*exams_average)
    print("Hi " + name + ". You have a " + grade + "% in your " + course + " course.")