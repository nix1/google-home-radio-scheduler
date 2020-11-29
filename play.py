from contextlib import contextmanager
from pychromecast import discovery, get_listed_chromecasts
import time


@contextmanager
def get_cast(device_name):
    for attempt in range(10):
        # List chromecasts on the network, but don't connect
        services, browser = discovery.discover_chromecasts()
        # Shut down discovery
        discovery.stop_discovery(browser)
        # Discover and connect to chromecasts
        chromecasts, browser = get_listed_chromecasts(friendly_names=[device_name])

        if len(chromecasts) == 0:
            discovery.stop_discovery(browser)
            backoff = 2**attempt
            print(f"Couldn't find {device_name}, retrying in {backoff}s...")
            time.sleep(backoff)
            # Retry
            continue

        cast = chromecasts[0]
        # Start worker thread and wait for cast device to be ready
        cast.wait()
        # Yield a ready-to-use cast object
        yield cast
        # Cleanup
        discovery.stop_discovery(browser)
        # Return, no need to retry
        return

    raise ConnectionError


def play_stream(device_name, url):
    with get_cast(device_name) as cast:
        mc = cast.media_controller
        mc.play_media(url, 'audio/mpeg')
        mc.block_until_active()
        mc.pause()
        time.sleep(5)
        mc.play()
