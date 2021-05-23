#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        v = list(a_dictionary.values())
        k = list(a_dictionary.keys())
        # Retorna la key en la posición de maximo valor en value
        return k[v.index(max(v))]
    else:
        return None
