#http://community.topcoder.com/stat?c=problem_statement&pm=12707

def maxSongs(duration, tone, time):
    avgTone = 1.0*sum(tone)/len(tone)
    songs = zip(duration, tone)
    songs = sorted(songs, key=lambda a: a[0] + abs(a[1] - avgTone))
    sang = []
    sangTime = 0
    count = 0
    while sangTime < time and songs:
        sang.append(songs.pop(0))
        sangTime = calcTime(sang)
        if sangTime <= time:
            count += 1
        avgSangTone = 1.0*sum([a[1] for a in sang])/len(sang)
        songs = sorted(songs, key=lambda a: a[0] + abs(a[1] - avgSangTone))
    return count
    
def calcTime(songs):
    songs = sorted(songs, key=lambda a: a[1])
    time = sum([a[0] for a in songs]) + abs(songs[0][1] - songs[-1][1])
    return time
    
maxSongs([5611,39996,20200,56574,81643,90131,33486,99568,48112,97168,5600,49145,73590,3979,94614], [2916,53353,64924,86481,44803,61254,99393,5993,40781,2174,67458,74263,69710,40044,80853], 302606) #8