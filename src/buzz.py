import board
import bitbangio
import adafruit_drv2605
i2c = bitbangio.I2C(board.SCL, board.SDA)
drv = adafruit_drv2605.DRV2605(i2c)
drv.use_ERM()
drv.set_waveform(14)
drv.play()
