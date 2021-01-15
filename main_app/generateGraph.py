import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import networkx as nx
import io
import numpy as np

from .models import Student, Friendship1

from django.db import connection

def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


def create_graph():   
    if(db_table_exists('student_table') and db_table_exists('friendship_table')):
        all_students = Student.objects.all()
        all_friendships  = Friendship1.objects.all()

        G = nx.DiGraph()

        for student in all_students:
            G.add_node(student.id)
        for friendship in all_friendships:
            G.add_edge(friendship.student.id, friendship.friend.id)

        degrees = [G.degree[a] for a in G.nodes]
        degrees_unique = sorted(list(set(degrees)))
        y_positions = {degrees_unique[i] : i for i in range(len(degrees_unique))}
        x_positions = {}

        for degree in degrees_unique:
            x_positions[degree] = [a for a in degrees.count(degree) / 2. - np.arange(degrees.count(degree))]

        positions = {}

        for node in G.nodes:
            deg = G.degree[node]
            positions[node] = (x_positions[deg].pop(), y_positions[deg])


        nx.draw_networkx(G, pos=positions, node_size=300)
        # nx.draw_networkx(G)
        buf = io.BytesIO()
        plt.savefig(buf, format='svg', bbox_inches='tight')
        image_bytes = buf.getvalue().decode('utf-8')
        buf.close()
        plt.close()
        return image_bytes
    else:
        return "No graph"