"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [int(row[1]) for row in data]
    suma = sum(list_s)
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [row[0] for row in data]
    list_s
    cnt = Counter()
    for word in list_s:
        cnt[word] += 1
    dic_list = dict(cnt)
    lista_or = []
    for key in sorted(dic_list.keys()):
        lista_or.append((key,dic_list[key]))
  
    return lista_or


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],row[1]) for row in data]
    counter = {}
    for key,value in list_s:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)
    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    return suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [row[2] for row in data]
    partes_fec = [line.split("-") for line in list_s]
    months = [row[1] for row in partes_fec]
    cnt = Counter()
    for mes in months:
        cnt[mes] += 1
    dic_list = dict(cnt)
    lista_or = []
    for key in sorted(dic_list.keys()):
        lista_or.append((key,dic_list[key]))
    return lista_or


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],row[1]) for row in data]
    counter = {}
    for key,value in list_s:
        if key in counter:
            if int(counter[key][0]) < int(value):
                counter[key][0] = int(value)
            elif int(counter[key][1]) > int(value):
                counter[key][1] = int(value)
        else:
            counter[key] = [int(value),int(value)]
    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    final = []
    for  key,value in suma:
        v = (key,value[0],value[1])
        final.append(v)
    return final


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    def descomp(x):
        """
        Funcion que extrae los valores de cada par string:valor
        """
        y = x.split(':')
        return y
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [row[4]for row in data]
    list_s_desc_1 =  [line.split(",") for line  in list_s]
    list_s_desc_2 = [descomp(elem) for row in list_s_desc_1 for elem in row ]
    list_s_desc_3 = [(row[0],int(row[1])) for row in list_s_desc_2 ]
    counter = {}
    for key,value in list_s_desc_3:
        if key in counter:
            if counter[key][1] < (value):
                counter[key][1] = (value)
            elif counter[key][0] > (value):
                counter[key][0] = (value)
        else:
            counter[key] = [(value),(value)]

    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    final = []
    for  key,value in suma:
        v = (key,value[0],value[1])
        final.append(v)
    return final


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],int(row[1])) for row in data]
    counter = {}
    for letra,numero in list_s:
        if numero in counter:
            counter[numero].append(letra)
        else:
            counter[numero] = [letra]
    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    return suma


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],int(row[1])) for row in data]
    counter = {}
    for letra,numero in list_s:
        if numero in counter:
            if letra in counter[numero]:
                continue
            else:
                counter[numero].append(letra)
        else:
            counter[numero] = [letra]
    suma = [(key,sorted(counter[key])) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    return suma


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    def descomp(x):
        """
        Funcion que extrae los valores de cada par string:valor
        """
        y = x.split(':')
        return y
    from collections import Counter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [row[4]for row in data]
    list_s_desc_1 =  [line.split(",") for line  in list_s]
    list_s_desc_2 = [descomp(elem) for row in list_s_desc_1 for elem in row ]
    list_s_desc_3 = [(row[0]) for row in list_s_desc_2 ]
    cnt = Counter()
    for word in list_s_desc_3:
        cnt[word] += 1
    dic_list = dict(cnt)
    dic_list = sorted(dic_list.items())
    counter = {}
    for key,value in dic_list:
        counter[key] = value
    return counter


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    def descomp_1(x):
        y = x.split(':')
        return y
    def descomp_2(x):
        y = x.split(',')
        return y
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],row[3],row[4])for row in data]
    list_s_desc_1 = [(elem[0],descomp_2(elem[1]),descomp_2(elem[2]))for elem in list_s ]
    list_s_desc_2 = [(elem[0],len(elem[1]),len(elem[2]))for elem in list_s_desc_1 ]
    
    return list_s_desc_2


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    def descomp_2(x):
        y = x.split(',')
        return y
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(int(row[1]),descomp_2(row[3]))for row in data]
    list_s_1 = [(row[0],row[1][i]) for row in list_s for i in range(0,len(row[1]))]
    counter = {}
    for value,key in list_s_1:
        if key in counter:
            counter[key] += value
        else:
            counter[key] = int(value)
    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    dicc = {}
    for key,value in suma:
        dicc[key] = value 
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    def descomp_1(x):
        y = x.split(':')
        return y
    def descomp_2(x):
        y = x.split(',')
        return y
    from operator import itemgetter
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [line.replace("\n", "") for line in data]
    data = [line.replace("\t", ";") for line in data]
    data = [line.split(";") for line in data]
    list_s = [(row[0],descomp_2(row[4]))for row in data]
    list_s_1 = [(row[0],descomp_1(row[1][i])) for row in list_s for i in range(0,len(row[1]))]
    list_s_2 = [(row[0],int(row[1][1])) for row in list_s_1]
    counter = {}
    for key,value in list_s_2:
        if key in counter:
            counter[key] += value
        else:
            counter[key] = value
    suma = [(key,counter[key]) for key in counter]
    suma = sorted(suma, key=itemgetter(0))
    dicc = {}
    for key,value in suma:
        dicc[key] = value 
    return dicc
