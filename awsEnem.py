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

    # Spark Session
    spark = SparkSession \
    .builder \
    .appName("DataSprintsPOC - ENEM 2017") \
    .getOrCreate()

    # Loading data frame
    df = spark.read.load("data/microdados_enem2017/Microdados Enem 2017/DADOS/MICRODADOS_ENEM_2017.csv",
                    format="csv", sep=";", inferSchema="true", header="true", mode="DROPMALFORMED",
                    encoding= "UTF-8")

    # At a glance, this analysis is going to focus on approved essays
    df = df.where("TP_STATUS_REDACAO = 1")

    # sample data with the features that matters most (for now...)
    sample = df.rdd.map(lambda x: (x.NU_INSCRICAO, x.SG_UF_RESIDENCIA, x.CO_MUNICIPIO_RESIDENCIA,x.CO_MUNICIPIO_ESC,
                              x.TP_SEXO, x.TP_COR_RACA , x.TP_ENSINO, x.TP_ESCOLA,
                              x.TP_ANO_CONCLUIU, x.TP_LINGUA, 
                              x.TP_DEPENDENCIA_ADM_ESC, x.NU_NOTA_CN, x.NU_NOTA_CH, x.NU_NOTA_LC,
                              x.NU_NOTA_MT, x.NU_NOTA_REDACAO))

    # Collecting...
    data = sample.collect()
    size = 200000
    windows = [i for i in range(size, len(data), size)]
    windows.append(len(data))
    old_window = 0

    # Inserting...
    for window in windows:
        batch = data[old_window : window]
        arguments = b','.join(Database.cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in batch)
        query = b'INSERT INTO public.enem2017("NU_INSCRICAO", "SG_UF_RESIDENCIA", "CO_MUNICIPIO_RESIDENCIA", "CO_MUNICIPIO_ESC", "TP_SEXO", "TP_COR_RACA", "TP_ENSINO", "TP_ESCOLA", "TP_ANO_CONCLUIU", "TP_LINGUA", "TP_DEPENDENCIA_ADM_ESC", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO") VALUES'  + arguments

        # Calling the insert query
        Database.insert(query)
        print("Inserted data from rows "+str(old_window)+" to "+str(window))
        logger.info("Inserted data from rows "+str(old_window)+" to "+str(window))

        old_window = window
    
    batch = data[old_window : len(data)]
    arguments = b','.join(Database.cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in batch)
    query = b'INSERT INTO public.enem2017("NU_INSCRICAO", "SG_UF_RESIDENCIA", "CO_MUNICIPIO_RESIDENCIA", "CO_MUNICIPIO_ESC", "TP_SEXO", "TP_COR_RACA", "TP_ENSINO", "TP_ESCOLA", "TP_ANO_CONCLUIU", "TP_LINGUA", "TP_DEPENDENCIA_ADM_ESC", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO") VALUES'  + arguments
    Database.insert(query)
    print("Inserted data from rows "+str(old_window)+" to "+str(window))
    logger.info("Inserted data from rows "+str(old_window)+" to "+str(len(data)))

    # Done!
    logger.info("Data inserted!")