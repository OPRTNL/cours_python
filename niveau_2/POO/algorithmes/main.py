# Renverser la valeur d'un chaine de ccaractère

c = "Bonjour toto"

def reverse_string(str):
    return str[::-1]

print(reverse_string(c))

# Trouver le min et le max d'une phrase

s = "Un chasseur sachant chasser doit savoir chasser sans son chien"

def min_max(s):
    result = s.split(" ")
    result.sort(key = lambda x : len(x))
    return (result[0], result[-1])

print(min_max(s))