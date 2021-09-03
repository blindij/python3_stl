import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commented = 2
    fix_release = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('\nMember value: {}'.format(BugStatus.wont_fix.value))
