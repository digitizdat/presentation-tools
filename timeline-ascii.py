#!/usr/bin/env python3
#
# timeline-ascii.py
#
# Create an ascii representation of a timeline, given the number of days
# between each event.
#
# You can take a screenshot of the ascii timeline and then scale it to any
# width, quickly giving you an accurate representation of spacing between
# events so you can create a graphical timeline using circles and lines (or
# whatever).
#
# USAGE: ./timeline-ascii.py days1 days2 ... daysN
#
# EXAMPLE: ./timeline-ascii.py 20 6 8 14 2 13 1 7 13 1
# ******************** ------ ******** -------------- ** ------------- * ------- ************* -
#

import sys
import click


@click.command(context_settings=dict(help_option_names=["-h", "-?", "--help"]))
@click.argument('days', nargs=-1)
def main(days):
    """Create an ascii representation of a timeline.

    DAYS is a list of days between each event.

    EXAMPLE: ./timeline-ascii.py 20 6 8 14 2 13 1 7 13 1
    """
    chars = ['*', '-']
    char = 0
    out = ''
    
    for day in days:
        out += chars[char]*int(day)
        char = (char+1) % 2
    
    print(out)
    pass


if __name__ == "__main__":
    main()
