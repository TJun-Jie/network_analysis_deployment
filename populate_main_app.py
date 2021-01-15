import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')

import django
django.setup()

#Fake script

import random 
from main_app.models import Student, Friendship1
from faker import Faker

fakegen =Faker()
# seed to generate 10 students
def add_student(N=10):
    for entry in range(N):
        student = fakegen.name()
        
        stu = Student.objects.get_or_create(name =student)[0]

        
# seed to add 2 friends for each student while selecting a popular kid
# every student will choose the popular student as their friend (except the popular student himself)
# other than that the student will choose his own friend
def add_friendship():
    # number_of_students = Student.objects.all().count()
    number_of_students = 40

    popular_kid_id = 23
    popular_kid = Student.objects.get(pk=popular_kid_id)

    for i in range(1, 1 + number_of_students ):
        student = Student.objects.get(pk=i)
        if(student):
            # add popular kid as friend 
            if( i != popular_kid_id):
                friendship  = Friendship1( student = student, friend = popular_kid)
                friendship.save()

                # List of random numbers without popular kid and student
                my_list = list(x for x in range(1, 1 + number_of_students +1) if x not in [popular_kid_id,i])
                random.shuffle(my_list)

                # Add random friend 1
                r_friend =Student.objects.get(pk=my_list[-1])
                friendship  = Friendship1( student = student, friend = r_friend)
                friendship.save()

                # Add random friend 2
                r_friend2 =Student.objects.get(pk=my_list[-2])
                friendship  = Friendship1(student = student, friend = r_friend2)
                friendship.save()

            # if the student is the popular kid, then add some random guy
            else:
                 # List of random numbers without popular kid and student
                my_list = list(x for x in range(1, 1 + number_of_students +1) if x not in [i])
                random.shuffle(my_list)

                # Add random friend 1
                r_friend =Student.objects.get(pk=my_list[-1])
                friendship  = Friendship1( student = student, friend = r_friend)
                friendship.save()

                # Add random friend 2
                r_friend2 =Student.objects.get(pk=my_list[-2])
                friendship  = Friendship1(student = student, friend = r_friend2)
                friendship.save()

                # Add random friend 3
                r_friend3 =Student.objects.get(pk=my_list[-3])
                friendship  = Friendship1(student = student, friend = r_friend3)
                friendship.save()

def show_students():
    number_of_students = Student.objects.all()
    for student in number_of_students:
        print(student.id)
    print("Total number:" , number_of_students.count())
    # all_friendships  = Friendship1.objects.all()
    # for friendship in all_friendships:
    #     print(friendship.student.name)
    #     print(friendship.friend.name)

    
if __name__ =='__main__':
    print('populating script!')
    add_student(40)
    # show_students()
    add_friendship()
    print("Populating complete!")