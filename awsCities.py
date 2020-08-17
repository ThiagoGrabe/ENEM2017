# Analysis Tools
from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
from Connection import Connection
import config as cred


if __name__ == "__main__":

    Database = Connection(
    user= cred.PGUSER,
    host= cred.PGHOST,
    database= cred.PGDATABASE,
    password= cred.PGPASSWORD)

    # Logger
    logger = Database.getLogger()

    # Loading data
    cities = pd.read_csv('data/cities/cidades.csv', names=['nameMun', 'codMun', 'bornMun', 'mainMun', 'area2018',
                                                      'PopMun2019', 'denMun2010', 'Esc6_to_14_2010', 'idhMun2010',
                                                      'ChildrenDeath_per1000born_2010', 'Incomex1000_2017',
                                                      'Costx1000_2017', 'PIB_percapita_2017'], skiprows=1, decimal=',')


    cities = cities.drop(['bornMun', 'mainMun', 'denMun2010', 'Esc6_to_14_2010', 'ChildrenDeath_per1000born_2010'], axis=1)

    # Cleaning some important features
    cities = cities.replace('-', '0')

    cities['idhMun2010'] = cities.idhMun2010.str.replace(',','.')
    cities['Incomex1000_2017'] = cities.Incomex1000_2017.str.replace(',','.')
    cities['Incomex1000_2017'] = cities.Incomex1000_2017.str.replace('Não informado','0')
    cities['Costx1000_2017'] = cities.Costx1000_2017.str.replace(',','.')
    cities['Costx1000_2017'] = cities.Costx1000_2017.str.replace('Não informado','0')

    cities.idhMun2010 = cities.idhMun2010.astype(float)
    cities.Incomex1000_2017 = cities.Incomex1000_2017.astype(float)
    cities.Costx1000_2017 = cities.Costx1000_2017.astype(float)

    # Some checking
    assert cities.dtypes.nameMun == 'O'
    print('Passed! nameMun type ' + str(cities.dtypes.nameMun))

    assert cities.dtypes.tolist()[1:] != 'O', "Type failure."
    print('Passed! All other types except nameMun should be numerical values')

    for value in cities.idhMun2010.tolist():
        assert value < 1 , "IDH should be more than one!"
    print('Passed! All idh values should be less than 1')

    for col in cities.columns:
        if cities[col].dtype != 'O':
    #         print('Feature '+ str(col) + ' is not numerical')
            for value in cities[col].tolist():
                assert value >= 0 , "Social numbers are greater than one."
    print('Passed! All social numbers are racional')

    # Inserting
    for i, record in cities.iterrows(): 
        rec = []
        for i in record:
            rec.append(i)
        query = '''INSERT INTO cities ("NA_MUNICIPIO_RESIDENCIA", "CO_MUNICIPIO_RESIDENCIA", "AREA_MUNICIPIO", "POP_MUNICIPIO", "IDH_MUNICIPIO", "INCOME_MUNICIPIO_X1000", "COST_MUNICIPIO_X1000", "PIP_MUNICIPIO_PER_CAPITA") VALUES ('{}', {}, {},{}, {}, {},{}, {})
            '''.format(str(rec[0]), int(rec[1]), rec[2], rec[3], rec[4], rec[5], rec[6], rec[7])

        Database.insert(query)
    print("\n\nInserted data from cities dataset")
    logger.info("Inserted data from cities dataset")