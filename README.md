## Udacity Data Engineering NanoDegree Project 5: Data Pipelines with Apache Airflow

#### Project rubric can be found here: https://review.udacity.com/#!/rubrics/2478/view

## Purpose

#### This project continues to follow the imaginary startup Sparkify as they expand their data architecture. Their processes have evolved to where they require a structred pipeline that can be updated and monitored.

## Data Model

#### Apache Airflow has been implemented as a solution that their team can use to gain control over their data.

#### The <code>dag.py</code> file contains a DAG that stages their song data to Redshift and creates the necessary fact and dimension tables. Finally, the DAG runs a task that performs quality checks on the data after all tables have been created and populated. This is done by several predefined and custom operators in the operators folder.The helpers folder contains SQL queries that are used to create the various fact and dimension tables.

