"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import os
import csv
import json
import pathlib
import errno
from pathlib import Path
from os import path
from models import NearEarthObject, CloseApproach


#neo_csv_path = pathlib.Path("./data/neos.csv")
#cad_json_path = pathlib.Path("./data/cad.json")

#global variable to data directory
data_dir = pathlib.Path(__file__).parent / 'data'


def load_neos(neo_csv_filename):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    #bring global variable into function
    global data_dir
    #use global variable to get path to filename in data directory
    neo_csv_path = data_dir / neo_csv_filename

    #verify csv file exists
    #if neo_csv_path.exists():
        #print(f"File \"{neo_csv_path.absolute()}\" exists")
    #else:
        #print(f"File \"{neo_csv_path.absolute()}\" does not exist")
        #raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), neo_csv_filename)

    list_neos = []
    
    #load and read csv data
    with open(neo_csv_path, 'r') as infile:
        csv_reader = csv.DictReader(infile, delimiter=',')

    #select specific csv columns
        for row in csv_reader: 
            #create neo object to add to list
            neo = NearEarthObject(
                    designation = row['pdes'],
                    name = row['name'], 
                    diameter = row['diameter'],
                    hazardous = row['pha']
            )
            list_neos.append(neo)

    # TODO: Load NEO data from the given CSV file.
    return list_neos


def load_approaches(cad_json_filename):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    #bring global variable into function
    global data_dir
    
    #use global variable to get path to filename in data directory
    cad_json_path = data_dir / cad_json_filename
        
    #verify json file exists
    if cad_json_path.exists():
        print(f"File \"{cad_json_path.absolute()}\" exists")
    else:
        print("File \"cad.json_path.absolute()}\" does not exist")
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), cad_json_filename)

    cad_data = []
    with open(cad_json_path, 'r') as json_data:

        #load json data
        data_load = json.load(json_data)

        #iterate through "data" tuples selecting des, cd, dist, v_rel
        for i in data_load["data"]:
            #create close approach object
            cad = CloseApproach(designation = i[0], 
                                time = i[3], 
                                distance = i[4], 
                                velocity = i[7]
            )
            #append the selected tuples
            cad_data.append(cad)

    return cad_data
