from play import play_stream

if __name__ == "__main__":
    stations = dict(
        nowyswiat='https://n10a-eu.rcs.revma.com/ypqt40u0x1zuv',
        tokfm='https://radiostream.pl/tuba10-1.mp3',
        baobab='http://stream.radiobaobab.pl:8000/radiobaobab.mp3'
    )
    station = stations['baobab']
    play_stream(device_name='Pizza', url=station)
