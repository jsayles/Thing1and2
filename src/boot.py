# This file is executed on every boot (including wake-boot from deepsleep)
import gc

# Disable the ESP debug statements
#import esp
#esp.osdebug(None)

# Web REPL
#import webrepl
#webrepl.start()

gc.collect()
