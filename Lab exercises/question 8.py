#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
#How long will bus journey take? Alternatively , you could run to university. You jog the first mile at 7mph; then
#run the next two at 15mph ; before jogging the last at 7mph again. Will this be quicker or slower then the bus?

mile=4
speed=25/60
time=mile/speed
print('your time in bus ',time)
time_spend_in_stop=10*2
total_time_in_bus=time+time_spend_in_stop
print('your total time in bus to reach university is ',total_time_in_bus)
mile1=1
speed1=7/60
time1=mile1/speed1
print('your jogging time in 1 mile is', time1)
mile2=2
speed2=15/60
time2=mile2/speed2
print('your jogging time in 2 mile is ',time2)
mile3=1
speed3=7/60
time3=mile3/speed3
print('your jogging time in last mile is', time3)
total_time_while_jogging=time1+time2+time3
print('total time while jogging')
if total_time_while_jogging>total_time_in_bus:
    print('travelling through bus is faster')
else:
    print('travelling through bus is slower')
