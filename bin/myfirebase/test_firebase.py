#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File test_firebase.py:
#           1. Class for upload and download of data in the firebase account.
# -*- coding: utf-8 -*-
import myfirebase
import json
from datetime import datetime
import time
import random
import calendar
from uuid import getnode as get_mac
# Year, month, dat
# inicio = datetime(2019, 6, 1)
user = {
    1: u"user1",
    2: u"user2",
    3: u"user3",
    4: u"user4",
    5: u"user5",
    6: u"user6",
    7: u"user7",
    8: u"user8",
    9: u"user9",
    10: u"user10",
}
email = {
    1: u"user1@gmail.com",
    2: u"user2@gmail.com",
    3: u"user3@gmail.com",
    4: u"user4@gmail.com",
    5: u"user5@gmail.com",
    6: u"user6@gmail.com",
    7: u"user7@gmail.com",
    8: u"user8@gmail.com",
    9: u"user9@gmail.com",
    10: u"user10@gmail.com",
}

n_mac = {
    1: u"60E3270178FB",
    2: u"70E3450178FB",
    3: u"80E3350178FB",
}
lastName = {
    1: u'Pérez',
    2: u"González",
    3: u"Dorta",
    4: u"Lemus",
}

work = {
    1: u"Gerencia",
    2: u"Administración",
    3: u"Cocina",
    4: u"Auxiliar Gerencia",
}

info = {
    1: u"Eficiente",
    2: u"Sale temprano los viernes",
    3: u"Trabaja de noche",
    4: u"Esta de Vacaciones",
}

r_mac = {
    1: {u"name": u"Device 1", u"mac": u"60E3270178FB"},
    2: {u"name": u"Puerta 2", u"mac": u"70E3450178FB"},
    3: {u"name": u"Puerta 5", u"mac": u"80E3350178FB"}
}


def my_mac():
    mac = get_mac()
    mac_aux = ''.join(('%012X' % mac)[i:i + 2]for i in range(0, 12, 2))
    return mac_aux


class TestFirebase:
    def __init__(self, register_this_moth,
                 register_this_week,
                 register_this_day,
                 today=datetime.now()):
        self.__db = myfirebase.MyFirebase()
        self.__today = today
        self.__register_this_moth = register_this_moth
        self.__register_this_week = register_this_week
        self.__register_this_day = register_this_day
        self.__cont_up = 0
        self.__amount_day = 10

    def getCont(self):
        return self.__cont_up

    def register_divice(self):
        for i in r_mac:
            self.__db.upload_testMac(r_mac.get(i))

    def register_new_user(self, c_user):
        for x in range(c_user):
            op_user = random.randint(1, 10)
            em = email.get(op_user)
            fn = user.get(op_user)
            ln = lastName.get(random.randint(1, 4))
            wp = work.get(random.randint(1, 4))
            ot_i = info.get(random.randint(1, 4))
            B827EB67E372 = { u'finger0': u'vwscXxxHKmmMKUnDUBL+XR6mKJ0qPls2BI/JrhIYjLYKXykyqlgiOyF+8uXowZ26EmBlK4tlcxZx0Vrf4WZfJppAVIhJdjlR0RQeSWapUOJZnSDBPKzBZpLtSfyv4eh508+T/BV09LlJE2lBmljphG/uzzlu7BId6yqoJ+3KBgdu0LJBRPvFD8kSxL38YCIVGZuV6wU4tZVPzgishp46q6a1EA2vLXXLCe/k+ZtsQ97CoTsHWeYTveFS7H8g1YrObC7g6eMmHy92CR5ARVIxw4LyFpZdWZLmOEI5YCvwCFF20Bpg0ZGpdFKAVn+8LClviyU7uGmIP048PAT8LJ7329XZmRJEjDUmzoZmjqoo1L5LaWFd2QWdw0+QFAkc4GZHCn0igMudxjzIdZQOkdQFJ/YatSFwjlUjb66P/mZfY1uIF6QjNIL+smLA4Oudq7xcBpU4D2WQuEobyYdp/fRridVsdMJmoNC7JWi508Q5Wz0qRvEW9Gn2hm+EAfM1LPXumAgN7b4QO2lg/QZOZmgi+1APLAfHzxxmeto/UHJyKjGD0zMx0BZdticsCabPNQEhWGDpoI/nQHxctzLHRf3kCZ3SWL9+me/LrrZyEjiLz9Ul17fq+V/jhrIxjdzHtZeznH5pHVXrtocDcYfhSICIHLoerqH4X74pXVY7JO2HCDsdFRDwk95/W+AO+L2XrrKUbBLMxe0DYecmlx1kkFRKTjPwzyOOagUHNjgAy+tQhto2eMAE5oRfkukjmJqWnDI2mjkVDYyG1r/TP/qits1Os3GKbbNVLWEYmM5S+Ad6PhGkkW98UGI+ia254aGgJCqYOV2JAvbBJcT+bgT4a5dhQmcW2QkutUfpQVGESaO/fBDQsKY6vCYYvt3VpAddDs6NvEPGH2wcAhaad6FUrMub8BOQfqSdwILC3R+mQNg3f3ws1GI0papYbteIe3LCZCk8s5ks9JW2fAl4TthLheE8S2GJbxNyKgFTY/QJd3vzGNa9Nx8wlKoRBmC0MNO2OITYFuT6hVMlM9TcdFLxnq70Gyymfyxbmhz0o2n3QRXfq2wncCUPxN2ARSRq3lTL6zC7N1endxlF1g8T/4SGJuA9qLICRjfFIk6l/yTjRwqRz7bLqTz+jWAv8cMORFBzcs4+QqHoPdJ6KM0HLzhP1CRIw2IlCRqCKerSsJOT50J1oqUwqF4EK99/s9k42HMAXDHRssC5Y+HUp2CLtTWQo7Ssum2kI/u1rN6HdQivtAgWoA8='} 
            B827EB67E372 = { u'B827EB67E372': B827EB67E372 }
            up_data = {
                u'emailId': em,
                u'firstName': fn,
                u'lastName': ln,
                u'workPosition': wp,
                u'otherInfo': ot_i,
                u'm_div': B827EB67E372
            }
            self.__db.upload_testUser(up_data)

    def run(self):
        self.register_this_date(self.__register_this_day, self.__today)
        amount_week = self.__register_this_week - self.__register_this_day
        self.register_week_without_this_date(amount_week, self.__today)
        amount_moth = self.__register_this_moth - self.__register_this_week
        self.register_this_month__without_this_week(
            amount_moth, self.__today)

    def register_this_month__without_this_week(self, amount, this_week):
        n_amount = amount
        start_moth = this_week.replace(day=1)
        after_moth = start_moth
        num_week = this_week.isocalendar()[1]
        while n_amount > 0:
            if start_moth != -1:
                if num_week != start_moth.isocalendar()[1]:
                    r = random.randint(0, n_amount)
                    n_amount = n_amount - r
                    after_moth = start_moth
                    self.register_this_week(r, start_moth)
                start_moth = self.next_week_of_mouth(start_moth)
            else:
                self.register_this_week(n_amount, after_moth)
                n_amount = 0
                # print(start_moth)

    def register_week_without_this_date(self, amount, this_date):
        n_amount = amount
        date_monday = self.start_of_this_week(this_date)
        next_day = date_monday.day
        next_date = date_monday.replace(day=next_day)
        last_day = self.last_day_mouth(date_monday)
        end_day = self.end_of_this_week(this_date).day
        while n_amount > 0:
            if this_date.day != next_date.day:
                r = random.randint(0, n_amount)
                self.register_this_date(r, next_date)
                n_amount = n_amount - r
            next_day += 1
            if((next_day <= last_day) & (next_day <= end_day)):
                date_monday = next_date
                next_date = next_date.replace(day=next_day)
            else:
                self.register_this_date(n_amount, next_date)
                n_amount = 0

    def last_day_mouth(self, date):
        return calendar.monthrange(date.year, date.month)[1]

    def _json_registre(self, date):
        # n_m = my_mac()
        n_m = n_mac.get(random.randint(1, 3))
        h = random.randint(0, 23)
        m = random.randint(0, 59)

        date = date.replace(hour=h, minute=m)
        jj=date.strftime('%b')
        print(jj)
        up_data = {
            u'timeStamps': time.mktime(date.timetuple()),
            u'day': int(date.strftime('%d')),
            u'month': int(date.strftime('%m')),
            u'nameMonth': date.strftime('%B'),
            u'nameDay': date.strftime('%A'),
            u'year': int(date.strftime('%Y')),
            u'hour': int(date.strftime('%H')),
            u'minute': int(date.strftime('%M')),
            u'mac': n_m
        }
        print(up_data)
        op = random.randint(1, 10)
        up_data[u'emailId'] = email.get(op)
        up_data[u'firstName'] = user.get(op)
        # send data
        self.__cont_up += 1
        self.__db.upload_date_test(up_data)
        # print(up_data)
        return up_data

    def register_this_date(self, amount, this_date):
        for i in range(amount):
            self._json_registre(this_date)
        # print(self._json_registre(date))

    def end_of_this_week(self, this_date):
        date = this_date
        next_month = date.month
        next_day = date.day + 1
        last_day = self.last_day_mouth(this_date)
        while((next_day < last_day) &
              (6 != date.weekday()) &
              (date.month == next_month)):
            date = date.replace(day=next_day)
            next_month = date.month
            next_day += 1
        return date

    def start_of_this_week(self, this_date):
        date = this_date
        next_month = date.month
        next_day = date.day - 1
        while((next_day > 1) &
                (0 != date.weekday()) &
                (date.month == next_month)):
            date = date.replace(day=next_day)
            next_month = date.month
            next_day -= 1
        return date

    def register_this_week(self, amount, this_week):
        n_amount = amount
        date_monday = self.start_of_this_week(this_week)
        next_day = date_monday.day
        next_date = date_monday.replace(day=next_day)
        last_day = self.last_day_mouth(date_monday)
        end_day = self.end_of_this_week(this_week).day
        while n_amount > 0:
            r = random.randint(0, n_amount)
            self.register_this_date(r, next_date)
            n_amount = n_amount - r
            next_day += 1
            if((next_day <= last_day) & (next_day <= end_day)):
                date_monday = next_date
                next_date = next_date.replace(day=next_day)
            else:
                self.register_this_date(n_amount, next_date)
                n_amount = 0

    def next_week_of_mouth(self, date):
        end = self.end_of_this_week(date)
        n_day = end.day + 1
        last_day = self.last_day_mouth(date)
        if last_day >= n_day:
            next_week = end.replace(day=n_day)
            return next_week
        else:
            return -1

    def register_this_month(self, amount, this_week):
        n_amount = amount
        start_moth = this_week.replace(day=1)
        after_moth = start_moth
        # num_week = self.__today.isocalendar()[1]
        while n_amount > 0:

            if start_moth != -1:
                r = random.randint(0, n_amount)
                n_amount = n_amount - r
                after_moth = start_moth
                self.register_this_week(r, start_moth)
                start_moth = self.next_week_of_mouth(start_moth)
            else:
                self.register_this_week(n_amount, after_moth)
                n_amount = 0
                # print(start_moth)


if __name__ == '__main__':
    # aux = TestFirebase(100, 30, 10)
    aux = TestFirebase(100, 40, 10)
    date = datetime(2019, 9, 18)
    # aux.register_this_date(10,date)
    # print(aux.next_week_of_mouth(date))
    # aux.register_new_user(20)
    # aux.register_divice()
    aux.run()
    # print(aux.getCont())
    # print(aux._start_of_this_week())
