import datetime

intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=5):
    result = []
    if seconds == 'Never':
        return '[#8E8E8E]Never'
    seconds = int(seconds - (datetime.datetime.now().timestamp()))

    if seconds < 0:
        return '[red]<!> DUE NOW'

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])