#!/usr/bin/env python3

"""satv2 - version 2 of the SAT tester.

This program quizzes people on SAT vocabulary.
"""

import pprint
import satjson

def main():
    """The main function, runs everything"""
    vs = satjson.marshal_ugly_file()
    pprint.pprint(vs[:5])
    
if '__main__' == __name__:
    main()

