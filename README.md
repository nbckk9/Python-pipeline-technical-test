# Intro

This project is a data pipeline that creates a graph which links some drugs with their mentions in in clinical trials, medical publications and journals.

It handles 3 sources of data : 
* A list of drugs (csv file)
* A list of medical publications associated to a scientific journal and to a publication date (separated between a csv file and a json file)
* A list of clinical trials associated to a scientific journal and to a publication date (csv file) 

It then outputs the graph as a json file.    

# Processing

Each data input is firstly preprocessed to clean it and to prepare it for the graph creation. 
Those steps are separated in 3 differents python files in the 'src' folder. 

The graph is then created with the ouputs of all the preprocessings. 


# Usage

This project was developped with Python 3.8.9.

You can clone this repo by downloading from github or simply clone it from your terminal : 
'''git clone https://github.com/nbckk9/Python_test_DE'''

To use this project, you need the pandas v1.4.2 library installed.

'''pip install -r requirements.txt'''

Then to run the data pipeline, make sure to be in the repo base folder and then run the main.py : 

'''python main.py'''


# To go further 

To make this data pipeline able to handle large volumes of data we could : 
* Partition the data input files to parallelize processings
* You could implement multithreading or multiprocessing and use multiple workers
* Pandas is not suited for large volumes of data, you could use Dask or PySpark for example
* In the code, you could split the graph creation step in two separate steps, one for pubmed and one for clinical trials and add an extra step of merging to create the complete graph

# Part 2 : SQL

Please find the 2 SQL queries in the 'sql' folder of this repo.
