from player import Player
from datetime import datetime
import json
import xml.etree.ElementTree as ET


class PlayerFactory:
    def to_json(self, players):
        """
            This function should transform a list of Player objects into a list with dictionaries.
        """
        return [{
            **player.__dict__,
            'date_of_birth': player.date_of_birth.strftime('%Y-%m-%d')
        } for player in players]

    def from_json(self, list_of_dict):
        """
            This function should transform a list of dictionaries into a list with Player objects.
        """
        return [Player(item['nickname'], item['email'], item['date_of_birth'], item['xp'], item['cls'])
                for item in list_of_dict]

    def from_xml(self, xml_string):
        """
            This function should transform a XML string into a list with Player objects.
        """
        result = []
        items = ET.fromstring(xml_string).findall("player")

        for item in items:
            result.append(
                Player(
                    item.find("nickname").text,
                    item.find("email").text,
                    item.find("date_of_birth").text,
                    int(item.find("xp").text),
                    item.find("cls").text
                )
            )

        return result

    def to_xml(self, list_of_players):
        """
            This function should transform a list with Player objects into a XML string.
        """
        result = "<data>"

        for player in list_of_players:
            root = ET.Element("player")

            nick = ET.SubElement(root, "nickname")
            nick.text = player.nickname

            email = ET.SubElement(root, "email")
            email.text = player.email

            db = ET.SubElement(root, "date_of_birth")
            db.text = player.date_of_birth.strftime('%Y-%m-%d')

            xp = ET.SubElement(root, "xp")
            xp.text = str(player.xp)

            cls = ET.SubElement(root, "cls")
            cls.text = player.cls

            xml_doc = ET.tostring(root).decode()
            result += xml_doc

        return result + "</data>"


    def from_protobuf(self, binary):
        """
            This function should transform a binary protobuf string into a list with Player objects.
        """
        pass

    def to_protobuf(self, list_of_players):
        """
            This function should transform a list with Player objects into a binary protobuf string.
        """
        pass

