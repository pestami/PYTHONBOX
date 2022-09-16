#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     12.09.2022
# Copyright:   (c) SESA237770 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import time
import requests


# GATEWAY_HOST = "http://192.168.0.1"
GATEWAY_HOST = "http://lisa-00001829.local"
GATEWAY_HOST = "http://192.168.1.136"



resp = requests.get(GATEWAY_HOST + "/api/leds").json()
leds_colors = resp["leds"]
for color in ["#FF0000", "#00FF00", "#0000FF", "#000000"]:
    # Put color to all LEDs
    for led_id in range(len(leds_colors)):
        requests.put(GATEWAY_HOST + "/api/leds/{id}".format(id=led_id), json={"rgb": color})
    time.sleep(1)