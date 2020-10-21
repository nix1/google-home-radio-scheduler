from pychromecast import discovery, get_listed_chromecasts
import time


def play_stream(device_name, url):
    # List chromecasts on the network, but don't connect
    services, browser = discovery.discover_chromecasts()

    # Shut down discovery
    discovery.stop_discovery(browser)

    # Discover and connect to chromecasts
    chromecasts, browser = get_listed_chromecasts(friendly_names=[device_name])
    cast = chromecasts[0]
    # Start worker thread and wait for cast device to be ready
    cast.wait()

    mc = cast.media_controller
    mc.play_media(url, 'audio/mpeg')
    mc.block_until_active()
    mc.pause()
    time.sleep(5)
    mc.play()

    # Shut down discovery
    discovery.stop_discovery(browser)
