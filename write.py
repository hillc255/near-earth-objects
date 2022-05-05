"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
"""
import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename, delimiter=","):

    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each
    outputrow corresponds to the information in a single close approach
    from the `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should
                     be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',',
                                lineterminator='\n')

        # write header into file first
        writer.writeheader()

        # iterate through results and add to output row
        for result in results:
            row_dict = {}

            row_dict['datetime_utc'] = result.time
            row_dict['distance_au'] = result.distance
            row_dict['velocity_km_s'] = result.velocity
            row_dict['designation'] = result.designation
            row_dict['name'] = result.neo.name
            row_dict['diameter_km'] = result.neo.diameter
            row_dict['potentially_hazardous'] = result.neo.hazardous

            writer.writerow(row_dict)


def write_to_json(results, filename):

    """Write an iterable of `CloseApproach` objects to a JSON file.
    The precise output specification is in `README.md`. Roughly, the output
    is a list containing dictionaries, each mapping `CloseApproach` attributes
    to their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
                     saved.
    """

    # opening file to where data should be saved
    with open(filename, 'w') as f:
        # list to capture iteration
        ouput = []
        # iteration through the results
        for result in results:
            # dict is dictionary serializing approaches
            # with embedded dictionary serialized neo
            results_dict = dict(
                datetime_utc=datetime_to_str(result.time),
                distance_au=result.distance,
                velocity_km_s=result.velocity,
                neo={
                    "designation": result.neo.designation,
                    "name": result.neo.name,
                    "diameter_km": result.neo.diameter,
                    "potentially_hazardous": result.neo.hazardous
                }
            )
            ouput.append(results_dict)
        # write iterated output to file f
        json.dump(ouput, f, indent=2)
