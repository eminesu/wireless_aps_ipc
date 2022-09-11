# importing the subprocess module
import subprocess
import re
import json
from wifi import Cell, Scheme

def get_wireless_APs():
	wireless_json={}
	wireless_list=[]

	networks = list(Cell.all('wlan0'))

	for network in networks:
		wireless_json_dict['ssid'] = network.ssid
		wireless_json_dict['snr'] = network.signal
		wireless_json_dict['channel'] = network.channel
		wireless_list.append(wireless_json_dict)


	wireless_json['access_points'] = wireless_list

	with open("access.json", "w") as outfile:
		file = json.dump(wireless_json, outfile)