# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Text explaining script usage
# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
#  ...
# Output:
#  Outputs fractional Julian Date
#
# Written by Sean Rockett
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = 'nan' # description of argument 1
month = 'nan' # description of argument 2
day = 'nan'
hour = 'nan'
minute = 'nan'
second = 'nan'

# parse script arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
else:
    print(\
    'Usage: '\
    'python3 ymdhms_to_jd.py year month day hour minute second'\
    )
    exit()

# write script below this line

JD = day - 32075 + 1461*(year + 4800 + (month - 14)/12)/4 + 367*(month - 2 - (month - 14)/12*12)/12 - 3*((year + 4900 + (month - 14)/12)/100)/4
JD_mid = JD - 0.5
D_frac = (second + 60*(minute + 60*hour))/86400
jd_frac = JD + D_frac

# print result
print(jd_frac)