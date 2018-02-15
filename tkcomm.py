"""
Common Functions.
"""

def calc_time(delta):
    """Calculate d, m, h, m, and s from an int value."""
    mins, secs = divmod(delta, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    return [days, hours, mins, secs]


def str_time(d, h, m, s):
    """Return a string formatted time stamp."""
    return "{:.0f}d {:.0f}h {:.0f}m {:.0f}s".format(d, h, m, s)