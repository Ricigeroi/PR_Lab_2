from player import Player
from datetime import datetime
import json
import xml.etree.ElementTree as ET
import player_pb2

class PlayerFactory:
    def to_json(self, players):
        """
            This function should transform a list of Player objects into a list with dictionaries.
        """
        return [{
            'nickname': player.nickname,
            'email': player.email,
            'date_of_birth': player.date_of_birth.strftime('%Y-%m-%d'),
            'xp': player.xp,
            'class': player.cls
        } for player in players]

    def from_json(self, list_of_dict):
        """
            This function should transform a list of dictionaries into a list with Player objects.
        """
        return [Player(item['nickname'], item['email'], item['date_of_birth'], item['xp'], item['class'])
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
                    item.find("class").text
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

            cls = ET.SubElement(root, "class")
            cls.text = player.cls

            xml_doc = ET.tostring(root).decode()
            result += xml_doc

        return result + "</data>"


    def from_protobuf(self, binary):
        """
            This function should transform a binary protobuf string into a list with Player objects.
        """
        playersList = player_pb2.PlayersList()
        playersList.ParseFromString(binary)
        result = []

        for player in playersList.player:
            player = Player(
                nickname=player.nickname,
                email=player.email,
                date_of_birth=player.date_of_birth,
                xp=player.xp,
                cls=player_pb2.Class.Name(player.cls)
            )

            result.append(player)

        return result

    def to_protobuf(self, list_of_players):
        """
            This function should transform a list with Player objects into a binary protobuf string.
        """
        result = []
        for item in list_of_players:
            player = player_pb2.PlayersList.Player()
            player.nickname = item.nickname
            player.email = item.email
            player.date_of_birth = datetime.strftime(item.date_of_birth, "%Y-%m-%d")
            player.xp = item.xp
            player.cls = player_pb2.Class.Value(item.cls)
            result.append(player)

        playersMessagesList = player_pb2.PlayersList(player=result)
        binaryData = playersMessagesList.SerializeToString()

        return binaryData

