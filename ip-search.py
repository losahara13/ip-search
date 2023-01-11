#coded by loshara13

import json
import os
import sys
import time
import colorama
import requests
from colorama import Fore, Back

try:
	from colorama import just_fix_windows_console
	just_fix_windows_console()
except:
	failed = True

api = 'http://ip-api.com/json/'
ip = None

try:
	print('Checking internet connection...'+Fore.YELLOW+' [-] '+Fore.RESET)
	time.sleep(1)
except:
	print('No internet connection'+Fore.RED+' [0] '+Fore.RESET)
	sys.exit(0)

print('Internet connecion test sucefully'+Fore.GREEN+' [1] '+Fore.RESET)

try:
	while True:
		ip = input("\nIP# ")
		data = requests.get(api+ip).json()
		print('[IP] -', data['query']+'\n')
		print('[Status] -', data['status']+'\n')
		print('[Country] -', data['country']+'\n')
		print('[Region] -', data['regionName']+'\n')
		print('[City] -', data['city']+'\n')
		print('[Latitude] -', data['lat'],'\n')
		print('[Longitude] -', data['lon'],'\n')
		print('[Timezone] -', data['timezone']+'\n')
		print('[ISP] -', data['isp']+'\n')
		print('[Organization] -', data['org']+'\n')
except KeyboardInterrupt:
	sys.exit(1)