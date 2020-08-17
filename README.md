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
5. - Looking at some social aspects, did self declared black people perform as well as self declared white people?
6. - Is gender also an important feature when looking to the scores?
7. - People from public schools perform at the same level as private schools?

At the end of this work, it will be presented some insights about the topic and the questions. Then, this work will try to answer all of them with some charts presentations to exemplify the results and support the arguments.


## Data Modeling

The data modeling for this project is simple and it is based on the following flow.

![Flow](https://github.com/ThiagoGrabe/ENEM2017/blob/master/img/ENEM2017%20-%20DataFlow.png)
