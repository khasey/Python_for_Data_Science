# La fonction filter(function, iterable)
# prend en entrée une fonction et un itérable.
# Elle retourne un nouvel itérable (spécifiquement un filtre)
# composé d'éléments pour lesquels la fonction renvoie True.

def ft_filter(function, iterable):
    '''This function returns a filter object'''
    # Nous utilisons une list comprehension pour parcourir chaque élément
    # de l'itérable Si la fonction renvoie True pour cet élément,
    # il est inclus dans la nouvelle liste
    return [item for item in iterable if function(item)]
    # item for item in iterable : Cela parcourt chaque élément de l'itérable.
    # if function(item) : C'est une condition qui vérifie si function(item)
    # renvoie True. Si c'est le cas, l'élément est inclus dans la liste.
    # return : Cela renvoie la liste.

# tester la fonction
# if __name__ == "__main__":
#     lst = [1, 2, 3, 4, 5]
#     print(list(ft_filter(lambda x: x % 2 == 0, lst)))
