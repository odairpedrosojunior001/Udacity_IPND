def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    if location<0:
        return somestring
    return part_before + part_after


print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"
