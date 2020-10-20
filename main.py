from play import play_stream
import schedule
import time

STATIONS = dict(
    nowyswiat='https://n10a-eu.rcs.revma.com/ypqt40u0x1zuv',
    tokfm='https://radiostream.pl/tuba10-1.mp3',
    baobab='http://stream.radiobaobab.pl:8000/radiobaobab.mp3'
)

DEVICE_NAME = 'Pizza'


def play_station(station_id):
    station = STATIONS[station_id]
    print(f"Starting the {station_id} radio station...")
    play_stream(device_name=DEVICE_NAME, url=station)


if __name__ == "__main__":
    schedule.every().monday.at("7:45").do(lambda: play_station("nowyswiat"))
    schedule.every().tuesday.at("7:45").do(lambda: play_station("nowyswiat"))
    schedule.every().wednesday.at("7:45").do(lambda: play_station("nowyswiat"))
    schedule.every().thursday.at("7:45").do(lambda: play_station("nowyswiat"))
    schedule.every().friday.at("7:45").do(lambda: play_station("nowyswiat"))

    while True:
        schedule.run_pending()
        time.sleep(10)
