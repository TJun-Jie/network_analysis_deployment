
from .models import Friendship1
from django.db import connection

def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

def num_friends(student_object):
    friends = Friendship1.objects.all()
    count = 0
    for entry in friends:
        if student_object == entry.friend:
            count +=1
    return count

def create_table():
    if(db_table_exists('friendship_table')):
        table_context ={}
        # Create tables for student,friend 1-3
        for entry in Friendship1.objects.all():
            if entry.student.id not in table_context.keys():
                name_list=[]
                name_list.append(entry.student.name)
                name_list.append(entry.friend.name)
                table_context[entry.student.id]=name_list
            else:
                table_context[entry.student.id].append(entry.friend.name)
        # Create tables for number of friends of student
        for entry in Friendship1.objects.all():       
            table_context[entry.student.id].append(num_friends(entry.student))

        return table_context
    else:
        return "No data found"

