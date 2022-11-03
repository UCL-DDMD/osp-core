"""An example explaining the API of CUDS objects."""

# Please install the lib ontology: $pico install lib

# If you did not install the city ontology
# (pico install lib),
# you have to execute these commands first:
# from osp.core import Parser
# p = Parser()
# p.parse("city")

from osp.core.utils import pretty_print
from osp.core.namespaces import lib

print("Creating a City object, c...")
c = lib.Electrode(name="cathode")
print("  uid of c: " + str(c.uid))
print("  IRI of c: " + str(c.iri))
print("  oclass of c: " + str(c.oclass) + "\n")

print("Creating Citizen objects, p1, p2...")
p1 = lib.Element(name="Li")
p2 = lib.Element(name="Mn")
print("  uid of p1: " + str(p1.uid))
print("  IRI of p1: " + str(p1.iri))
print("  oclass of p1: " + str(p1.oclass) + "\n")
print("  uid of p2: " + str(p2.uid))
print("  IRI of p2: " + str(p2.iri))
print("  oclass of p2: " + str(p2.oclass) + "\n")

print("Checking attributes of the CUDS objects...")
print(f"Name of c: {c.name}.")
print("Name of p1: " + str(p1.name))
print("Name of p2: " + str(p2.name))

#print("\nChanging the attribute values of the CUDS objects...")
print(f"Change the name of {p1.name}.")
p1.name = "K"
print(f"Name of p1: {p1.name}.")

print("\nAdding p1 to c...")
c.add(p1, rel=lib.HAS_PART)
print("this has been added to the electrode material")

for el in c.iter():
    print("  uid: " + str(el))

print("\nGetting p1 from c:")
#print(c.get(p1.uid))

print("IRI of c :" + str(c.iri))
pretty_print(c)
c.elements
#print("\nGetting lib.Element from c:")
#print(c.get(oclass=lib.Element))
#
#print("\n Remove p1:")
#c.remove(p1.uid)
#print("internal dict of c:", c._Element, "\n")
#
#print("\nAdding neighborhoods to Cuds object in a loop:")
#for i in range(6):
#    print("Added neighborhood %s" % i)
#    c.add(city.Neighborhood(name="neighborhood %s" % i))
#print("internal dict of c:", c._neighbors, "\n")
#
#print("Trying out the `is_a` method trivially with the new neighborhoods.")
#print(all(n.is_a(city.Neighborhood) for n in c.get(oclass=city.Neighborhood)))
#