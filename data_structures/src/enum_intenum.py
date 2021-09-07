import enum

class BugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commented = 2
    fix_release = 1

print('Ordered by value:')
print('\n'.join(''+s.name for s in sorted(BugStatus)))
