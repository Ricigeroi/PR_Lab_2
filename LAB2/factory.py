from player import Player
from datetime import datetime
import json

class PlayerFactory:
    def to_json(self, players):
        '''
            This function should transform a list of Player objects into a list with dictionaries.
        '''
        return [{
            **player.__dict__,
            'date_of_birth': player.date_of_birth.strftime('%Y-%m-%d')
        } for player in players]

    def from_json(self, list_of_dict):
        '''
            This function should transform a list of dictionaries into a list with Player objects.
        '''
        return json.dumps(list_of_dict)

    def from_xml(self, xml_string):
        '''
            This function should transform a XML string into a list with Player objects.
        '''
        pass

    def to_xml(self, list_of_players):
        '''
            This function should transform a list with Player objects into a XML string.
        '''
        pass

    def from_protobuf(self, binary):
        '''
            This function should transform a binary protobuf string into a list with Player objects.
        '''
        pass

    def to_protobuf(self, list_of_players):
        '''
            This function should transform a list with Player objects into a binary protobuf string.
        '''
        pass

