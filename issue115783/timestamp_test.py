from datetime import datetime
#from dateutil.parser import isoparse
import sys

'''
Issue 115783 of cpython
Since Python 3.11, datetime.fromisoformat(...) accepts invalid timestamps.
The same code was tested in many Python versions via GitHub Actions:

Wrong format: 2024-01-17T15:21:00-0800
Fixed format: 2024-01-17T15:21:00-08:00
'''

# correct run
def test_correct1():
    try:
        datetime.fromisoformat("2024-01-17T15:21:00-08:00")
        # True positive
        print("test_correct1 - PASSED")
    except ValueError:
        # False negative trigger [incorrect]
        print("test_correct1 - FAILED")

def test_fails(in_stamp, i):
    try:
        datetime.fromisoformat(in_stamp)
        # False positive
        print(f"test_fail{i} - FAILED")
    except ValueError:
        # True negative trigger [incorrect]
        print(f"test_fail{i} - PASSED")


def fail_driver():
    stamps = ["2024-01-17T15:21:00-0800", "2024-01-17T15:21:00-0800", "2024-01-17T152100-08:00", \
            "20240117T15:21:00-08:00", "2024-01-17T152100-0800", \
            "20240117T15:21:00-0800", "20240117T152100-08:00"]
    i = 0
    for s in stamps:
        test_fails(s, i)
        i += 1


# MAIN
print(f"Python version {sys.version}")
test_correct1()
fail_driver()
#util_driver()