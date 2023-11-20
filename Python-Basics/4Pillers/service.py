from SA import *
from CA import *


def get_service(obj):
    print(obj.cal_bal())


get_service(SA(104, 'Priyanka', 'priya@gmail.com', 'marathahalli', 1000))
get_service(CA(204, 'Kamall', 'kamla@gmail.com', 'Chnnai', 30000))
get_service(Account('gopi', 'gopi@academy.com', 'Hyd'))
