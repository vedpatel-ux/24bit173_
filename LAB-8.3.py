names_set = set()

names_set.update(["ved", "jinit", "jeet", "prem", "naman", "Vidit"])

print("Set after adding names:", names_set)

if "Vidit" in names_set:
    names_set.remove("Vidit")
    names_set.add("Manav")

print("Set after modifying a name:", names_set)

names_set.remove("ved")
names_set.remove("prem")

print("Set after deleting two names:", names_set)