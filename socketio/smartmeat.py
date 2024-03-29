import json
import random
import os
import logging
import sys

from singleton import Singleton
from datetime import datetime
from pytz import timezone


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@Singleton
class Smartmeat():

    def __init__(self, on=False, temperature=-100, sticks=[]):
        self.on = on
        self.temperature = temperature
        self.sticks = {
            "stick1": {
                "active": False,
                "time_active": "00:00:00"
            },
            "stick2": {
                "active": False,
                "time_active": "00:00:00"
            },
            "stick3": {
                "active": False,
                "time_active": "00:00:00"
            },
            "stick4": {
                "active": False,
                "time_active": "00:00:00"
            }
        }


    def __str__(self):
        return self.serialize()


    def __dict__(self):
        new_dict = {
                "on": self.on,
                "temperature": self.temperature,
                "stick1": {
                    "active": self.sticks['stick1']['active'],
                    "time_active": self.sticks['stick1']['time_active'],
                },
                "stick2": {
                    "active": self.sticks['stick2']['active'],
                    "time_active": self.sticks['stick2']['time_active'],
                },
                "stick3": {
                    "active": self.sticks['stick3']['active'],
                    "time_active": self.sticks['stick3']['time_active'],
                },
                "stick4": {
                    "active": self.sticks['stick4']['active'],
                    "time_active": self.sticks['stick4']['time_active'],
                }
            }
        return new_dict


    def set_state(self, on):
        self.on = on


    def set_temperature(self, value):
        if value >= 1 and value <= 4:
            self.temperature = value
        else:
            logger.info("ERROR: Invalid temperature value: {}".format(value))


    def set_stick(self, stick_number):
        tz = timezone('Brazil/East')
        now = datetime.now(tz=tz)
        curr_time = '{0:%H:%M:%S}'.format(now)
        self.sticks[stick_number] = {
            "active": True,
            "time_active": curr_time
        }


    def remove_stick(self, stick_number):
        self.sticks[stick_number] = {
            "active": False,
            "time_active": "00:00"
        }


    def get_active_sticks(self):
        states = []
        for _, v in self.sticks.items():
            states.append(v['active'])

        # return list with position of all active sticks
        return [idx+1 for idx, val in enumerate(states) if val == True]


    def serialize(self):
        json_str = {}
        json_str["\"smartmeat\""] = json.dumps(self.__dict__())
        return json_str
