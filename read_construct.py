##Kevin Chen ID:49859223

import app_handler
import output_generator


def user_interface():

    num_outputs = 0

    '''inputs'''
    number_of_locations = int(input())    
    start_location = input()
    end_locations = _input_end_locations(number_of_locations)
    num_outputs = int(input())


    '''outputs'''
    json_file = app_handler._generate_json(start_location, end_locations)
    _generate_and_print_outputs(num_outputs, json_file)       

    print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")



def _input_end_locations(number_of_locations:int)-> [str]:
    '''takes in number of locations and asks users for the legs of the
    trip'''
    end_locations = []
    
    for i in range(number_of_locations-1):
        end_locations.append(input())

    return end_locations


def _generate_and_print_outputs(num_outputs:int, result:'json') -> None:
    '''allows user to ask for outputs and prints out requested outputs'''

    output_list = []

    output_dictionary = {
        'STEPS': output_generator.directions(result),
        'TOTALDISTANCE': output_generator.total_distance(result),
        'TOTALTIME': output_generator.total_time(result),
        'LATLONG': output_generator.long_lat(result)
    }

    for j in range(num_outputs):
        output_list.append(input())

    for map_input in output_list:
        output_dictionary[map_input].generate()



if __name__ == '__main__':
    user_interface()
    
