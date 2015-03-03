#!/usr/bin/env python

import string
import random
import hashlib

def make_cookie_str(user, time):
    return user + "|" + time

def make_hash(user, time):
    return hashlib.md5(make_cookie_str(user, time)).hexdigest()[0:10]

def random_username(m, n):
    random_len = random.randint(m, n)
    return ''.join([random.choice(string.ascii_lowercase) for _ in xrange(random_len)])

def random_date():
    return str(random.randint(0, 20150227)).zfill(8)

q = 2**20
R = {}
for i in xrange(q):
    date = random_date()
    R[make_hash("mikero", date)] = make_cookie_str("mikero", date)

while True:
    user = random_username(1, 20)
    h = make_hash(user, "20150227")

    if h in R:
        print make_cookie_str(user, "20150227") + " == " + R[h]
