import time

weekly_playlist = ["Blinding Lights","Levitating","As It Was","Heat Waves","Good 4 u"]
i = 0
while i < 5:
    weekly_playlist.append(weekly_playlist[0])
    weekly_playlist.pop(0)
    print(weekly_playlist)
    i += 1
    time.sleep(2)
print("The playlist has ended")