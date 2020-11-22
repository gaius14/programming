
def sum_list(the_list):
    total = 0
    for item in the_list:
        total = total + item
    return total 
    
    
# inizializzo una lista vuota per salvare i valori
values = []
# apro e leggo il file, linea per linea
my_file = open("shampoo_sale.cvs", "r")
for line in my_file:
    # faccio lo split di ogni riga sulla virgola 
    elements = line.split(',')
    
    # se NON sto processando l'intestazione...
    if elements[0] != 'Date':
        # setto la data e il valore 
        date = elements[0]
        value = elements[1]
        # aggiungo alla lista dei valori questo valore 
        values.append(float(value))
        
csv_data_sum = sum_list(values)

print(csv_data_sum)
