from pychromecast.discovery import discover_chromecasts, stop_discovery
from pychromecast.controllers import BaseController
from pychromecast import Chromecast
import pychromecast
import time

# config
device_name = 'Pizza'
rns = 'https://n10a-eu.rcs.revma.com/ypqt40u0x1zuv'

# List chromecasts on the network, but don't connect
services, browser = discover_chromecasts()


# Shut down discovery
stop_discovery(browser)

# Discover and connect to chromecasts
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[device_name])
cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()

print(cast.device, cast.status)

mc = cast.media_controller
mc.play_media(rns, 'audio/mpeg')
mc.block_until_active()
print(mc.status)
mc.pause()
time.sleep(5)
mc.play()


# Shut down discovery
pychromecast.discovery.stop_discovery(browser)
