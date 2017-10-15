import ev
import prep
from add import addSegment
from brut import BruteForceList

def rbSegIntersection(red, blue, visit):
    nr = len(red)
    nb = len(blue)
    n = nr + nb
    ne = 2 * n

    events = prep.prepareEvts(red, blue)
    # console.log(unpack(events))

    redList  = BruteForceList(nr)
    blueList = BruteForceList(nb)
    ret = False
    for i in xrange(0, ne):
        e, index = int(events[i][1]), int(events[i][2])
        if e == ev.CREATE_RED:
            ret = addSegment(index, red, redList, blue, blueList, visit, False)
        elif e == ev.CREATE_BLUE:
            ret = addSegment(index, blue, blueList, red, redList, visit, True)
        elif e == ev.REMOVE_RED:
            redList.remove(index)
        elif e == ev.REMOVE_BLUE:
            blueList.remove(index)

        if ret:
            break
    return ret
