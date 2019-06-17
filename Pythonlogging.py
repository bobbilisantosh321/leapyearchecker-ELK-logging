import logging
import logstash

host = '18.208.210.179'

test_logger = logging.getLogger('python-logstash-log')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))

# Python program to check if the input year is a leap year or not

# To get year (integer input) from the user
# year = int(input("Enter a year: "))
def leapYear(year):
    if (year <= 0):
        test_logger.error('leapyear-checker: {0} is a not a valid year.'.format(year))
    else:
        test_logger.info('leapyear-checker: Validating leap year for {0}'.format(year))
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    test_logger.info("leapyear-checker: {0} is a leap year".format(year))
                else:
                    test_logger.warning("leapyear-checker: {0} is not a leap year".format(year))
            else:
                test_logger.info("leapyear-checker: {0} is a leap year".format(year))
        else:
            test_logger.error('leapyear-checker: This is not a leap year')


leapYear(101)
leapYear(1991)
leapYear(-1996)
leapYear(2019)
leapYear(-121)