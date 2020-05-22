from System import Guid

g = Guid.NewGuid()
print("Hello! Your Python-made GUID is: {}".format(g))

def new_guid():
    return Guid.NewGuid()