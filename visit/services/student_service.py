from visit.models import Student, Guest
"""
SOLID
Single responsibility principle
Open-close principle
Liskov substitution principle
Interface Segregation principle
Dependency invertion principle  
"""
def get_student(student_id: str) -> Student | None:
    try:
       return Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        pass  # Handle the case where the student doesn't exist


def increment_student_visits(guest: Guest, student: Student):
    guest.student_visited = student
    guest.save()
