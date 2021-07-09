class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name=name 
    
    def get_data(self):
        #inizializzo una lista vuota dove salvo i valori
        values=[]
       
        #provo ad aprire il file e leggere riga per riga
        try:
            my_file=open(self.name, 'r')
        except:
            raise ExamException('il file non esiste oppure non è leggibile')
        
        for line in my_file:
            #faccio lo split di ogni riga sulla virgola
            elements=line.split(',')
            #se non sto processando l'intestazione
            if elements[0]!='epoch':
                #setto l'epoch e la temperatura
                epoch=elements[0]
                temperature=elements[1]
                values.append([int(float(epoch)), float(temperature)])
        
        #controllo che la lista sia ordinata
        for i in range (0,len(values)-1):
            if values[i][0]>=values[i+1][0]:
                raise ExamException('lista non ordinata')
                
        #controllo che non ci siano timestamp dublicati
        for j in range (i+1, len(values)):
            if values[j][0]==values[i][0]:
                raise ExamException('timestamp duplicato')
        
        #chiudo il file
        my_file.close()
        return values

def compute_daily_max_difference(time_series):
    #inizilizzo una lista vuota dove salvare il valore di differena massima di ogni giorno
    values_max_diff=[]
   
    #inizializzo un indice nullo che userò in seguito per ricavare i vari valori 
    index=0

    if len(time_series)==1:
        values_max_diff=None
        #perché la differenza massima tra le rilevazioni di temperatura non si può calcolare con una sola temperatura
    
    while (index<len(time_series)):
        #calcolo l'inizio e la fine del giorno
        start_day=time_series[index][0]-(time_series[index][0]%86400)
        end_day=start_day+86400

        min=time_series[index][1]
        max=time_series[index][1]

        #uso l'indice dichiarato in precedenza per ricavare i valori delle giornate
        while(index<len(time_series)and time_series[index][0]<end_day):
            if (min>=time_series[index][1]):
                min=time_series[index][1]
            if (max<=time_series[index][1]):
                max=time_series[index][1]
            
            #incremento
            index+=1
        
        max_diff=max-min

        values_max_diff.append(max_diff)
    #print(len(values_max_diff))
    return values_max_diff

#questa classe si dovrà quindi poter usare così:
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()

#stampo l'escrusione termica dei vari giorni
print(compute_daily_max_difference(time_series))
