import os, platform

try:

    import requests

except:

    os.system('pip install requests')

bit = platform.architecture()[0]

if bit == '64bit':

    import Haroon

    

elif bit == '32bit':

    import Haroon32
