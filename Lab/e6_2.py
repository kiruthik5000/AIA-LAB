import collections
import collections.abc

collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable

from kanren import Relation, facts, run, var, conde

doctor = Relation()
treats = Relation()

# Facts
facts(doctor,
    ("dr_smith",),
    ("dr_jones",),
    ("dr_lee",),
    ("dr_williams",),
    ("dr_davis",)
)

facts(treats,
    ("dr_smith", "flu"),
    ("dr_smith", "allergy"),
    ("dr_jones", "cold"),
    ("dr_lee", "covid"),
    ("dr_lee", "pneumonia"),
    ("dr_williams", "diabetes"),
    ("dr_davis", "hypertension")
)

def is_skilled(person):
    return conde((doctor(person), treats(person, var())),)

x = var()

disease = input("Enter the disease").strip()

result = run(0, x, treats(x, disease))
if result:
    print("✓ Skilled doctors found:")
    for name in result:
        print(f"- {name.replace('_', ' ').title()}")
else:
    print("X No skilled doctors found.")

