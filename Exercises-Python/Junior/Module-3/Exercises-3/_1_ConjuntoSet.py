# CONJUNTO SET

# elementos unicos
frutas = {"manzana", "banana", "pera", "kiwi", "manzana"}

print(frutas)

# Crear un conjunto set desde una lista (elimina duplicados)
frutas_lista = ["manzana", "banana", "pera", "kiwi", "manzana", "piña"]
print(frutas_lista)
frutas_dict = set(frutas_lista)
print(frutas_dict)

# OPERACIONES DE CONJUNTOS SET
# Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("\nUNION: "), print(A | B), print(A.union(B))


# Interseccion
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("\nINTERSECCION: "), print(A & B), print(A.intersection(B))


# Diferencia
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("\nDIFERENCIA: "), print(A - B), print(A.difference(B)), print(B.difference(A))
# print(A.difference(B)): Que esta en A que no este en B. print(B.difference(A)): Que esta en B que no este en A.


# Diferencia simetrica
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("\nDIFERENCIA SIMETRICA: "), print(A ^ B), print(A.symmetric_difference(B))
# print(A.symmetric_difference(B)): Que esta en A que no este en B y de B que no este en A