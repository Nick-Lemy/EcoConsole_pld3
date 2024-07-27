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
        return total_footprint

class ClimateAdvice:
    @staticmethod
    def give(footprint):
        print("\n** Climate Advice **")
        if footprint < 100:
            print("Great job! Your carbon footprint is low. Keep up the good work!")
        elif 100 <= footprint < 500:
            print("You're doing okay, but there's room for improvement. Consider reducing your car travel or using energy-efficient appliances.")
        else:
            print("Your carbon footprint is high. Try to reduce your energy consumption and car travel. Consider renewable energy sources and more sustainable practices.")
        print("********\n")

class ClimateConsoleApp:
    @staticmethod
    def get_carbon_footprint_inputs():
        electricity = float(input("\nEnter your monthly electricity usage (kWh): "))
        gas = float(input("Enter your monthly gas usage (therms): "))
        car_miles = float(input("Enter your monthly car travel (miles): "))
        return electricity, gas, car_miles

    def main(self):
        print("\n====================================")
        print("\033[1;34m Welcome to the Climate Console App \033[0m")
        print("\033[1;32m====================================\033[0m")

        while True:
            print("\n--------- Menu ---------")
            print("1. Receive Notification")
            print("2. Calculate Carbon Footprint")
            print("3. Get Climate Advice")
            print("4. Donate or Watch an Advertisement")
            print("5. Exit")
            print("------------------------\n")        
