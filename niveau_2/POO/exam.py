"""

def addition(data):
    
    if not data or len(data) == 0:
        return None
    
    for d in data:
        d += d
    return d

print(addition(()))
a = input()
i = int(a)

while i > 0:
    print(i)
    i -= 1

    """

age = 17

if age == 17:
    print("coucc")
elif age >= 18:
    print("mes ocuilles")
else:
    print("tu l'as vu?")


def get_description():
    pass

get_description()