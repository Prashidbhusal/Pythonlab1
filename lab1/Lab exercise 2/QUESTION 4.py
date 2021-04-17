#IF TEMPERATURE IS GREATER THEN 30, IT'S A HOT DAY OTHERWISE IF IT'S LESS THEN 10;
#IT'S A COLD DAY; OTHERWISE , IT'S NEITHER HOT NOR COLD.

temperature=float(input('Enter the temperature'))
if temperature>10:
    print('its hot')
elif temperature<10:
    print('its cold')
else:
    print('its neither hot nor cold')