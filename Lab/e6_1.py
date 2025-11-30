import collections
import collections.abc

# Fix for Python 3.10+
collections.Iterator = collections.abc.Iterator
collections.Hashable = collections.abc.Hashable

from kanren import Relation, facts, run, var, conde

# Knowledge base: hospital scenario
doctor = Relation()
treats = Relation()

# Facts: doctors
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
