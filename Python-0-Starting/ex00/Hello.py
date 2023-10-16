ft_list = ["Hello", "tata!"]
#Les listes sont mutables, donc vous pouvez directement modifier leurs éléments.
ft_tuple = ("Hello", "toto!")
#Les tuples sont immutables, ce qui signifie que vous ne pouvez pas modifier 
# un tuple existant. Au lieu de cela, vous devez créer un nouveau tuple avec les valeurs souhaitées.
ft_set = {"Hello", "tutu!"}
#Pour les ensembles (sets), vous pouvez ajouter ou supprimer des éléments, mais vous ne pouvez pas les modifier directement.
ft_dict = {"Hello" : "titi!"}
#Pour les dictionnaires, vous pouvez directement modifier la valeur associée à une clé.

ft_list = ft_list[:1] + ["World!"]
ft_tuple = ft_tuple[:1] + ("France",)
ft_set = {item for item in ft_set if item != "tutu!"} | {"Mulhouse"}
ft_dict["Hello"] = "42Mulhouse"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)