from play import play_stream
import schedule
import time
import yaml

STATIONS = dict(
    nowyswiat='https://n10a-eu.rcs.revma.com/ypqt40u0x1zuv',
    tokfm='https://radiostream.pl/tuba10-1.mp3',
    baobab='http://stream.radiobaobab.pl:8000/radiobaobab.mp3'
)


def play_station(station_id, device_name):
    station_url = STATIONS[station_id]
    print(f"Starting the {station_id} radio station, playing on {device_name}...")
    play_stream(device_name=device_name, url=station_url)


if __name__ == "__main__":
    with open('schedule.yml') as schedule_file:
        schedule_config = yaml.safe_load(schedule_file)

    for day, jobs in schedule_config.items():
        for job in jobs:
            station = job['station']
            at = job['at']
            device = job['device']
            print(f"{day}: scheduling {station} for {at} on {device}")
            scheduler = getattr(schedule.every(), day)
            scheduler.at(at).do(play_station, station, device)

    print("👌 all fine, now just waiting...")
    while True:
        schedule.run_pending()
        time.sleep(10)
