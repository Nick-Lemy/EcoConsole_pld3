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

    def __init__(self, electricity, gas, car_miles):
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
            choice = input("Enter your choice: ")

            if choice == '1':
                Notification.send("Remember to turn off lights when not in use!")
            elif choice == '2':
                electricity, gas, car_miles = self.get_carbon_footprint_inputs()
                carbon_footprint = CarbonFootprint(electricity, gas, car_miles)
                footprint = carbon_footprint.calculate()
                print(f"\nYour total monthly carbon footprint is: {footprint:.2f} kg CO2")
                Notification.send(f"Your carbon footprint has been calculated: {footprint:.2f} kg CO2")
            elif choice == '3':
                electricity, gas, car_miles = self.get_carbon_footprint_inputs()
                carbon_footprint = CarbonFootprint(electricity, gas, car_miles)
                footprint = carbon_footprint.calculate()
                ClimateAdvice.give(footprint)
            elif choice == '4':
                self.donate_or_advertise()
            elif choice == '5':
                print("\nExiting the Climate Console App. Goodbye!\n")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.\n")

            # Pause for 3 seconds before showing the menu again
            time.sleep(3)

    @staticmethod
    def donate_or_advertise():
        print("\nWould you like to:")
        print("1. Donate")
        print("2. Watch an Advertisement")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nTo donate, please use this number: +250793246060")
        elif choice == '2':
            ads = [
                "https://youtu.be/bzlLVpWTyvU?si=zPUdpZdp_40w1SG0",
                "https://youtu.be/X2waKapmfCY?si=6G57cgS8YUBw-8z3",
                "https://youtu.be/ZbM4arzTdug?si=ZvpKJpqVh_ULuh2T",
                "https://youtu.be/gZ9cOKVkmfg?si=H0PcSiWv75naHJ1s",
                "https://youtu.be/TI-fLK-1km4?si=AMrxyd5IAAdVT_dO"
            ]

            ad_link = random.choice(ads)
            print(f"\nWatch this advertisement: {ad_link}")

            # Open the advertisement link in the default web browser
            webbrowser.open(ad_link)
        else:
            print("\nInvalid choice. Please enter 1 or 2.\n")

        # Pause for 3 seconds before showing the menu again
        time.sleep(3)

if __name__ == "__main__":
    app = ClimateConsoleApp()
    app.main()
