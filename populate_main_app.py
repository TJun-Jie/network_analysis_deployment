import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','network_project.settings')

import django
django.setup()

#Fake script

import random 
from main_app.models import Student, Friendship1
from faker import Faker
from django.contrib.auth.models import User

fakegen =Faker()
# seed to generate 10 students
def add_student(N=10):
    for entry in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_username = fake_firstname[:2]+fake_lastname[:-2]
        fake_pass= 'Junjie2000'

        users = User.objects.create_user(username=fake_username,first_name=fake_firstname,last_name=fake_lastname)
        u=User.objects.get(username=fake_username)
        u.set_password(fake_pass)
        u.save()
        
# seed to add 2 friends for each student while selecting a popular kid
# every student will choose the popular student as their friend (except the popular student himself)
# other than that the student will choose his own friend
def add_friendship():
    all_students = User.objects.filter(is_staff=False)
    first_student_id = all_students[0].id
    number_of_students = all_students.count()
    print(first_student_id)
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

def show_students():
    number_of_students = User.objects.filter(is_staff=False)
    for student in number_of_students:
        print(student)
    print("Total number:" , number_of_students.count())
    # all_friendships  = Friendship1.objects.all()
    # for friendship in all_friendships:
    #     print(friendship.student.name)
    #     print(friendship.friend.name)
    print(User.objects.filter(is_staff=False))

def delete_all_friendships():
    delele_all_friendships = Friendship1.objects.all().delete()
    User.objects.filter(is_staff=False).delete()
    
    

def show_friend_with_id(id):
    print(Friendship1.objects.filter(student__id = id))

#reset password for all students
def reset_all_password():
    all_students = User.objects.filter(is_staff=False)
    for entry in all_students:
        entry.set_password('Junjie2000')
        entry.save()
if __name__ =='__main__':
    print('populating script!')
    add_student(40)
    # show_students()
    add_friendship()
    # delete_all_friendships()
    # show_friend_with_id(30)
    # reset_all_password()
    print("Populating complete!")