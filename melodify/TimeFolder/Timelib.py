class Time:
    def __init__(self ,h , m, s):
        self.h = h
        self.m = m
        self.s = s

    def playlistLength(songList):
        hh = 0 
        mm = 0
        ss = 0
        for song in songList:
            time = song.time
            hh += time.h
            mm += int(time.m)
            if mm > 59:
                mm -= 60 
                hh += 1
            ss += int(time.s)
            if ss > 59:
                ss -= 60
                mm += 1
        print(f'playlist length: {hh}h {mm}m {ss}s')  