from play import play_stream
import schedule
import time
import yaml
import validators

with open('stations.yml') as stations_file:
    STATIONS = yaml.safe_load(stations_file)


def play_station(station, device_name):
    print(f"Starting the {station['name']} radio station, playing on {device_name}...")
    play_stream(device_name=device_name, url=station['url'])


def main():
    with open('schedule.yml') as schedule_file:
        schedule_config = yaml.safe_load(schedule_file)

    for day, jobs in schedule_config.items():
        for job in jobs:
            station = STATIONS[job['station']]
            at = job['at']
            device = job['device']
            print(f"{day.capitalize()}: scheduling {station['name']} for {at} on {device}")
            assert validators.url(station['url'])
            scheduler = getattr(schedule.every(), day)
            try:
                scheduler.at(at).do(play_station, station, device)
            except ConnectionError:
                print(f"Failed to connect to {device}")

    print("👌 all fine, now just waiting...")
    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()
