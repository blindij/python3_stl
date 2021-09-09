import calendar

# The default is to use the European convention of starting
# a week on Monday. The example show weeks starting on Sunday
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2021,9)
