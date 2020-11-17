
#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#venga inizializzato sul nome del file csv, e
#abbia un attributo “name” che ne contenga il nome
#abbia un metodo “get_data” che torni i dati dal file CSV come numeri di una lista (come abbiamo già visto).


# oggetto CSVFile
#  - init(filename)
#  - name
#  - get_data ()
#    return dati


class CSVFile:
    pass
    def __init__(self, filename):
        self.filename = filename


mio_file = CSVFile(filename='shampoo_sales.csv')

print(mio_file.filename)