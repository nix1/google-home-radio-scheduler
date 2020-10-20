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
    print(mc.status)
    mc.pause()
    time.sleep(5)
    mc.play()

    # Shut down discovery
    discovery.stop_discovery(browser)


if __name__ == "__main__":
    stations = dict(
        nowyswiat='https://n10a-eu.rcs.revma.com/ypqt40u0x1zuv',
        tokfm='https://radiostream.pl/tuba10-1.mp3',
        baobab='http://stream.radiobaobab.pl:8000/radiobaobab.mp3'
    )
    station = stations['baobab']
    play_stream(device_name='Pizza', url=station)
