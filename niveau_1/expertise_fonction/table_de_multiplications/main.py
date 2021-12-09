def show_result(index, base, result):
    print(index, " x ", base, " = ", result)

def multiplication(index, base):
    return index*base

def table_de_multiplication(table_de : int, min = 1, max = 10):
    if min > max : 
        print("ERREUR : Le minimun est supérieur au Maximum")
        return

    for i in range(min, max + 1):
        result = multiplication(i, table_de)
        show_result(i, table_de,result)
    
    print("************* Fin de la Table ********************")

table_de_multiplication(2, 100, 10)