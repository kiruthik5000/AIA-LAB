import collections
import collections.abc
from kanren import Relation, facts, run, var, conde

doctor = Relation()
treats = Relation()

facts(doctor,
    ("dr_smith",),
    ("dr_jones",),
    ("dr_lee",),
    ("dr_williams",),
    ("dr_davis",)
)

# Facts: diseases treated
facts(treats,
    ("dr_smith", "flu"),
    ("dr_smith", "allergy"),
    ("dr_jones", "cold"),
    ("dr_lee", "covid"),
    ("dr_lee", "pneumonia"),
    ("dr_williams", "diabetes"),
    ("dr_davis", "hypertension")
)
