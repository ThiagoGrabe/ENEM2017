# Data Analysis ENEM 2017


![ENEM2017](img/enem-2017.png)

This project is an analysis for ENEM 2017 data. All data are public and the information here is not confidential.

This notebook is structured as follow:

    1. Loading data;
    2. Data cleaning and selection using Pyspark framework;
    3. Creating Postgresql database on AWS;
    4. Data selection and feature engineering;
    5. Presentation on Power BI
    
    
## Analysis goal

In order to achieve the proposed milestones, some features will not be used or even analysed. This work consists on an analysis fo two main aspects of ENEM 2017:

    * Student score on all subjects per region and city
    * Social aspects and how it is realated to the performance.
    
With these two aspects, I intend to give an understanding of the following questions:

1. - What is the average of scores by city and state?
2. - Is there and bias related to the state? Can we realate to some other feature?
3. - What cities present the best and the worst results?
4. - What about the population size? Does it impact on the results?
5. - Looking at some social aspects, how self declaration is related to the final score?
6. - Is gender also an important feature when looking to the scores?
7. - People from public schools perform at the same level as private schools?

At the end of this work, it will be presented some insights about the topic and the questions. Then, this work will try to answer all of them with some charts presentations to exemplify the results and support the arguments.


## Data Modeling

The data modeling for this project is simple and it is based on the following flow.

![Flow](https://github.com/ThiagoGrabe/ENEM2017/blob/master/img/ENEM2017%20-%20DataFlow.png)

In this work, the data is prepared locally using [Pyspark](https://spark.apache.org/docs/latest/api/python/index.html) to have Apache Spark as a distributed framework that can handle Big Data analysis. I also use the [Postgresql](https://www.postgresql.org/) on a [AWS RDS instance](https://aws.amazon.com/pt/rds/postgresql/?trk=ps_a131L0000083bBMQAY&trkCampaign=pac_ps_Q1_120_RDS_PDP_P_NBrand_BR&sc_channel=ps&sc_campaign=pac_q1-1-2020_paidsearch_RDS_OpenSource_BR&sc_outcome=PaaS_Digital_Marketing&sc_geo=LATAM&sc_country=BR&sc_publisher=Google&sc_category=Database&sc_detail=postgres&sc_content=postgresql_e&sc_matchtype=e&sc_segment=448680794859&sc_medium=PAC-PaaS-P|PS-GO|Non-Brand|Desktop|PA|Database|RDS|BR|PT|Text&s_kwcid=AL!4422!3!448680794859!e!!g!!postgres&ef_id=CjwKCAjw1ej5BRBhEiwAfHyh1DPYrvfUO0dzYrntUhupo-dV_jUJiIBZ3yXwRd6xNMQW6GSEsOgvSBoCLEQQAvD_BwE:G:s&s_kwcid=AL!4422!3!448680794859!e!!g!!postgres) to access the data on the cloud storage system.

After some feature selection this analysis will be consisted on the final ENEM scores. In other words, the students who have not completed the exam and are eliminated from College selection process or cannot conclude the brazilian high school, they have the scored dropped and they are no longer in the database. This approach is important to cut outliers from data and examinate only people who attended to the exam.

| Features  | Type |
| ------------- | ------------- |
|NU_INSCRICAO           |float64|
|SG_UF_RESIDENCIA       |string|
|CO_MUNICIPIO_RESIDENCIA|int|
|CO_MUNICIPIO_ESC|int|
|TP_SEXO|int|
|TP_COR_RACA|int|
|TP_ENSINO|int|
|TP_ESCOLA|int|
|TP_ANO_CONCLUIU|int|
|TP_LINGUA|int|
|TP_DEPENDENCIA_ADM_ESC|int|
|NU_NOTA_CN|float|
|NU_NOTA_CH|float|
|NU_NOTA_LC|float|
|NU_NOTA_MT|float|
|NU_NOTA_REDACAO|float|

### Database - Postgresql

The database is very simple and has a main table called _enem2017_ and 5 auxiliar tables to have attributes and social aspects. The database architecture is described below:

1. _enem2017_ Table

| Feature  | Type |
| ------------- | ------------- |
|NU_INSCRICAO           |bigint (__PK__)|
|SG_UF_RESIDENCIA       |text|
|CO_MUNICIPIO_RESIDENCIA|numeric|
|CO_MUNICIPIO_ESC|numeric|
|TP_SEXO|numeric|
|TP_COR_RACA|numeric|
|TP_ENSINO|numeric|
|TP_ESCOLA|numeric|
|TP_ANO_CONCLUIU|numeric|
|TP_LINGUA|numeric|
|TP_DEPENDENCIA_ADM_ESC|numeric|
|NU_NOTA_CN|numeric|
|NU_NOTA_CH|numeric|
|NU_NOTA_LC|numeric|
|NU_NOTA_MT|numeric|
|NU_NOTA_REDACAO|numeric|

2. _cities_ Table:

| Feature  | Type |
| ------------- | ------------- |
|CO_MUNICIPIO_RESIDENCIA  |bigint (__PK__)|
|AREA_MUNICIPIO       |numeric|
|POP_MUNICIPIO|numeric|
|IDH_MUNICIPIO|numeric|
|INCOME_MUNICIPIO_X1000|numeric|
|COST_MUNICIPIO_X1000   |numeric|
|PIB_MUNICIPIO_PER_CAPITA|numeric|

3. _anoEnem_ Table:

| Feature  | Type |
| ------------- | ------------- |
|TP_ANO_CONCLUIU       |numeric (__PK__)|
|DESCRICAO|text|

4. _ensinoTipo_ Table:

| Feature  | Type |
| ------------- | ------------- |
|TP_ENSINO       |numeric (__PK__)|
|DESCRICAO|text|

5. _corRaca_ Table:

| Feature  | Type |
| ------------- | ------------- |
|TP_COR_RACA       |numeric (__PK__)|
|DESCRICAO|text|

6. _escolaTipo Table:

| Feature  | Type |
| ------------- | ------------- |
|TP_DEPENDENCIA_ADM_ESC       |numeric (__PK__)|
|DESCRICAO|text|


## How To

To access the data and the analysis it is necessary to download the Power BI report

    * [ENEM 2017 - POWER BI REPORT](https://github.com/ThiagoGrabe/ENEM2017/blob/master/enem2017_Report.pbix)
    
The database is instanciated on AWS RDS. All configuration properties are set in the [config.py](https://github.com/ThiagoGrabe/ENEM2017/blob/master/config.py) file.

If you want to recriate the database the following frameworks/packages are necessary:

    * Python 3.6
        - pyspark
        - numpy
        - pandas
        - matplotlib
        - xlrd
        - seaborn
        - jupyter
        
     * Postgresql 12
        - All queries are stored in the [query.txt](https://github.com/ThiagoGrabe/ENEM2017/blob/master/query.txt) file.
        
     * Power BI Desktop
     
 
     
 ## Results
 
 Some results are important to present. Brazil is a huge country with many different regions and social aspects. It is a unique and beautiful country, but also uneven.
 
 
