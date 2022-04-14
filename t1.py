from HW5_task1 import Teacher, Student, Homework
import datetime

teacher = Teacher('cher', 'tea')
student = Student('dent', 'stu')
true_homework = Homework('second_homework', datetime.timedelta(1))
false_homework = Homework('first_homework', datetime.timedelta(-1))


def test_create_homework():
    assert true_homework.text + false_homework.text == 'second_homework' + 'first_homework'


def test_deadline_homework():
    assert true_homework.deadline.days + false_homework.deadline.days == 0


def testing_deadline():
    assert true_homework.is_active() == True
    assert false_homework.is_active() == False


def testing_returned_homework(capsys):
    student.do_homework(false_homework)
    assert capsys.readouterr().out == "You are late\n"


def testing_names():
    assert teacher.first_name + student.last_name == "teadent"