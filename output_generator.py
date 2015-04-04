##Kevin Chen ID:49859223

class directions:
    '''this class is to generate the steps of the directions when
    generate is called'''
    def __init__(self, json_result):
        self._json_result = json_result
    
    def generate(self):
        print('')
        print("DIRECTIONS")
        for item in self._json_result['route']['legs']:
            for item2 in item['maneuvers']:
                print(item2['narrative'])


class total_distance:
    '''this class is to generate the total distance when generate is called'''
    def __init__(self, json_result):
        self._json_result = json_result

    def generate(self):
        print('')
        string = self._json_result['route']['distance']
        print('Total Distance: ' + str(round(string)) + ' miles')


class total_time:
    '''this class is to generate the total time of the trip when generate
    is called'''
    def __init__(self, json_result):
        self._json_result = json_result

    def generate(self):
        print('')
        string = self._json_result['route']['time']
        print('Total Time: ' + str(round(string/60)) + ' minutes')


class long_lat:
    '''this class is to generate the longitude and latitude of the legs
    of the trip when generate is called'''
    def __init__(self, json_result):
        self._json_result = json_result

    def generate(self):
        print('')
        for item in self._json_result['route']['locations']:
            string1 = item['latLng']['lat']
            string2 = item['latLng']['lng']
            print(str(string1) + 'N ' + str(string2) +'W')
