"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

from filters import HazardousFilter


def write_to_csv(results, filename, delimiter = ","):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    # TODO: Write the results to a CSV file, following the specification in the instructions.

    #import os
    #filename = 'results.csv'
    #print(f'writing to {filename} in {os.getcwd()}')

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ',', lineterminator='\n')
        
        # write header
        writer.writeheader()
   
        #Example:
        #datetime_utc,distance_au,velocity_km_s,designation,name,diameter_km,potentially_hazardous
        #2025-11-30 02:18,0.397647483265833,3.72885069167641,433,Eros,16.84,False
    
        for cla in results:
            row_dict = {}

            row_dict['datetime_utc'] = cla.time
            row_dict['distance_au'] = cla.distance
            row_dict['velocity_km_s'] = cla.velocity
            row_dict['designation'] = cla.designation
            row_dict['name'] = cla.neo.name
            row_dict['diameter_km'] = cla.neo.diameter
            row_dict['potentially_hazardous'] = cla.neo.hazardous

            writer.writerow(row_dict)
            #print("{}".format(row_dict))
 

#A missing name must be represented by the empty string (not `'None'`). 
#A missing diameter must be represented either by the empty string or by the string `'nan'`. 
#The `potentially_hazardous` flag should be either the string `'False'` or the string `'True'`.

         

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    
    #print(results)


#(CloseApproach(time='2020-01-01 00:54', distance=0.02, velocity=5.62, neo=NearEarthObject(designation='2020 AY1', name=None, diameter=nan, hazardous=False)), 
#CloseApproach(time='2020-01-01 02:06', distance=0.04, velocity=7.36, neo=NearEarthObject(designation='2019 YK', name=None, diameter=nan, hazardous=False)), 
#CloseApproach(time='2020-01-01 03:31', distance=0.16, velocity=2.79, neo=NearEarthObject(designation='2013 EC20', name=None, diameter=nan, hazardous=False)),
##CloseApproach(time='2020-01-01 07:18', distance=0.16, velocity=4.15, neo=NearEarthObject(designation='2020 AM1', name=None, diameter=nan, hazardous=False)), 
#CloseApproach(time='2020-01-01 08:44', distance=0.28, velocity=17.55, neo=NearEarthObject(designation='2016 EF195', name=None, diameter=nan, hazardous=False))
    
    #convert objects into json
    #data.json  = approach in results iteration

    #make CloseApproach JSON serializable
    #or construct something which is serializable like list of dictionaries
    #appending to list then dumping 
    

    #write json to out_file 
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2) #ensure_ascii=False, indent=2)