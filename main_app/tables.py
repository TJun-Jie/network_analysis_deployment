
from .models import Friendship1
from django.db import connection

def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_table():
    if(db_table_exists('main_app_friendship1')):
        friends = Friendship1.objects.all()
        table_context ={}
        # Create tables for student,friend 1-3
        for entry in friends:
            if entry.student.id not in table_context.keys():
                name_list=[]
                name_list.append(entry.student.name)
                name_list.append(entry.friend.name)
                table_context[entry.student.id]=name_list
            else:
                table_context[entry.student.id].append(entry.friend.name)
        # Create tables for number of friends of student
        number_of_friends = {}
        for entry in friends: 
            if(entry.student.name not in number_of_friends):
                number_of_friends[entry.student.id] = 0

        for entry in friends:
            number_of_friends[entry.friend.id] += 1

        for key in number_of_friends:
            table_context[key].append(number_of_friends[key])
        # print(table_context)
        return table_context
    else:
        return "No data found"

