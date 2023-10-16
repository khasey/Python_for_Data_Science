import datetime

# Obtenir le timestamp actuel
current_time = datetime.datetime.now()
timestamp = current_time.timestamp()
#cette ligne prend la valeur de timestamp,
# la formate pour utiliser des virgules 
# comme séparateurs des milliers et 
# arrondit à 4 décimales après la virgule,
# puis stocke le résultat dans la variable
# formatted_timestamp.
formatted_timestamp = '{:,.4f}'.format(timestamp)
print(f"Seconds since January 1, 1970: {formatted_timestamp} or {timestamp:.2e} in scientific notation")

print(current_time.strftime('%b %d %Y'))
