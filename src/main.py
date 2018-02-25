#####################################################################
# Main program run after Boot
#####################################################################

import time
import machine
import settings
import vibe
import led

# Hardware Test
led.cycle()
vibe.pulse()
