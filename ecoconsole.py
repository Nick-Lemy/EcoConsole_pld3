#!/usr/bin/python3

import time
import random
import webbrowser


class Notification:
    @staticmethod
    def send(message):
        print(f"\n*** Notification **\n{message}\n\n")
