#!/usr/bin/python3

import time
import random
import webbrowser


class Notification:
    @staticmethod
    def send(message):
        print(f"\n*** Notification **\n{message}\n\n")
        
class CarbonFootprint:
    CO2_PER_KWH = 0.92  # kg CO2 per kWh
    CO2_PER_THERM = 5.3  # kg CO2 per therm
    CO2_PER_MILE = 0.404  # kg CO2 per mile

    def _init_(self, electricity, gas, car_miles):
        self.electricity = electricity
        self.gas = gas
        self.car_miles = car_miles

    def calculate(self):
        electricity_footprint = self.electricity * self.CO2_PER_KWH
        gas_footprint = self.gas * self.CO2_PER_THERM
        car_footprint = self.car_miles * self.CO2_PER_MILE
        total_footprint = electricity_footprint + gas_footprint + car_footprint
        return total_footprint
