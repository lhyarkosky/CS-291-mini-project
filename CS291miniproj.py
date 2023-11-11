import tkinter as tk
import networkx as nx

class AcademicProgram:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_course(self, course, prerequisites=None):
        self.graph.add_node(course.upper())
        if prerequisites:
            for prereq in prerequisites:
                self.graph.add_edge(prereq.upper(), course.upper())

    def courses_without_prerequisites(self):
        return [course for course in self.graph.nodes() if len(self.graph.in_edges(course)) == 0]

    def courses_with_most_prerequisites(self):
        max_prerequisites = max([len(self.graph.in_edges(course)) for course in self.graph.nodes()])
        return [course for course in self.graph.nodes() if len(self.graph.in_edges(course)) == max_prerequisites]

    def courses_with_least_prerequisites(self):
        min_prerequisites = min([len(self.graph.in_edges(course)) for course in self.graph.nodes()])
        return [course for course in self.graph.nodes() if len(self.graph.in_edges(course)) == min_prerequisites]

    def has_circular_dependencies(self):
        try:
            nx.topological_sort(self.graph)
            return False
        except nx.NetworkXUnfeasible:
            return True



def add_course():
    course = course_entry.get()
    prerequisites_str = prerequisite_entry.get()
    prerequisites = prerequisites_str.split(",") if prerequisites_str else []
    academic_program.add_course(course, prerequisites)
    course_entry.delete(0, 'end')
    prerequisite_entry.delete(0, 'end')

def find_courses_without_prerequisites():
    result_label.config(text=academic_program.courses_without_prerequisites())

def find_courses_with_most_prerequisites():
    result_label.config(text=academic_program.courses_with_most_prerequisites())

def find_courses_with_least_prerequisites():
    result_label.config(text=academic_program.courses_with_least_prerequisites())

def find_circular_dependencies():
    if academic_program.has_circular_dependencies():
        result_label.config(text="Circular dependencies found")
    else:
        result_label.config(text="No circular dependencies")

academic_program = AcademicProgram()

window = tk.Tk()
window.title("Academic Program Analyzer")

course_label = tk.Label(window, text="Course:")
course_label.pack()

course_entry = tk.Entry(window)
course_entry.pack()

prerequisite_label = tk.Label(window, text="Prerequisites (comma-separated):")
prerequisite_label.pack()

prerequisite_entry = tk.Entry(window)
prerequisite_entry.pack()

add_button = tk.Button(window, text="Add Course", command=add_course)
add_button.pack()

find_without_prereq_button = tk.Button(window, text="Courses without prerequisites", command=find_courses_without_prerequisites)
find_without_prereq_button.pack()

find_most_prereq_button = tk.Button(window, text="Courses with most prerequisites", command=find_courses_with_most_prerequisites)
find_most_prereq_button.pack()

find_least_prereq_button = tk.Button(window, text="Courses with least prerequisites", command=find_courses_with_least_prerequisites)
find_least_prereq_button.pack()

find_circular_button = tk.Button(window, text="Check for Circular Dependencies", command=find_circular_dependencies)
find_circular_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
