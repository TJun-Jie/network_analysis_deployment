import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')

from faker import Faker
fakegen = Faker()

import django
django.setup()
from django.contrib.auth.models import User


from main_app.models import Student, Friendship1
import random


def add_friendship():
    all_students = User.objects.filter(is_staff=False)
    first_student_id = all_students[0].id
    print(all_students)
    print(first_student_id)
    number_of_students = all_students.count()
    popular_kid_id = first_student_id + 10
    popular_kid = User.objects.get(pk=popular_kid_id)

    for i in range(first_student_id, first_student_id + number_of_students ):
        student = User.objects.get(pk=i)
        if( not student.groups.filter(name="admin").exists() and student):

            # add popular kid as friend 
            if( i != popular_kid_id):
                friendship  = Friendship1( student = student, friend = popular_kid)
                friendship.save()

                # List of random numbers without popular kid and student
                my_list = list(x for x in range(first_student_id, first_student_id+ number_of_students ) if x not in [popular_kid_id,i])
                random.shuffle(my_list)

                # Add random friend 1
                r_friend =User.objects.get(pk=my_list[-1])
                friendship  = Friendship1( student = student, friend = r_friend)
                friendship.save()

                # Add random friend 2
                r_friend2 =User.objects.get(pk=my_list[-2])
                friendship  = Friendship1(student = student, friend = r_friend2)
                friendship.save()

            # if the student is the popular kid, then add some random guy
            else:
                 # List of random numbers without popular kid and student
                my_list = list(x for x in range(first_student_id, first_student_id + number_of_students ) if x not in [i])
                random.shuffle(my_list)

                # Add random friend 1
                r_friend =User.objects.get(pk=my_list[-1])
                friendship  = Friendship1( student = student, friend = r_friend)
                friendship.save()

                # Add random friend 2
                r_friend2 =User.objects.get(pk=my_list[-2])
                friendship  = Friendship1(student = student, friend = r_friend2)
                friendship.save()

                # Add random friend 3
                r_friend3 = User.objects.get(pk=my_list[-3])
                friendship  = Friendship1(student = student, friend = r_friend3)
                friendship.save()

if __name__ == "__main__":
    print("adding friendships")
    add_friendship()
    print("adding friendships complete")