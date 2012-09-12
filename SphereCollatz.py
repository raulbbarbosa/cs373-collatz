#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing & Raul B. Barbosa
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {190735 : 223,
811713 : 62,
393879 : 100,
61637 : 149,
449452 : 113,
995689 : 215,
677664 : 155,
102418 : 80,
306007 : 97,
648850 : 93,
201203 : 112,
881607 : 176,
792824 : 163,
763147 : 132,
715297 : 49,
988624 : 60,
569420 : 178,
506255 : 183,
883010 : 96,
490640 : 152,
632849 : 142,
919625 : 140,
696020 : 124,
947294 : 127,
781833 : 101,
246220 : 151,
144948 : 70,
158203 : 101,
633578 : 103,
41173 : 32,
649065 : 80,
273626 : 177,
7497 : 63,
32067 : 47,
314799 : 110,
685384 : 305,
504587 : 227,
253894 : 58,
104160 : 80,
983941 : 171,
85819 : 103,
594587 : 147,
13864 : 33,
368955 : 136,
249924 : 151,
224729 : 50,
360628 : 66,
826539 : 114,
919908 : 96,
561555 : 209,
382239 : 136,
184839 : 210,
339218 : 123,
341461 : 53,
101117 : 204,
163477 : 96,
308163 : 159,
966349 : 47,
226448 : 156,
393082 : 131,
56182 : 48,
946611 : 101,
971955 : 96,
223329 : 68,
127321 : 106,
523031 : 165,
74094 : 144,
246546 : 182,
742487 : 88,
731191 : 181,
128042 : 49,
361564 : 66,
818475 : 207,
235797 : 50,
668655 : 155,
7435 : 45,
247883 : 58,
733685 : 88,
558388 : 116,
709715 : 199,
499108 : 152,
20 : 8,
735380 : 88,
414468 : 69,
321177 : 53,
538570 : 72,
991733 : 215,
212246 : 81,
238496 : 76,
618319 : 142,
838080 : 83,
295477 : 159,
256190 : 226,
130488 : 132,
653919 : 93,
6780 : 182,
121156 : 168,
609995 : 204,
681408 : 62,
657526 : 292,
775714 : 75,
100147 : 67,
878298 : 65,
256741 : 58,
192542 : 73,
375773 : 87,
658038 : 62,
796858 : 163,
259355 : 270,
867648 : 44,
893152 : 140,
381120 : 149,
24146 : 44,
874012 : 189,
275132 : 84,
558519 : 134,
888850 : 264,
174253 : 73,
556868 : 85,
258698 : 151,
73641 : 170,
747720 : 119,
506241 : 183,
792734 : 75,
482191 : 121,
82870 : 64,
66756 : 118,
346929 : 79,
589503 : 266,
832152 : 132,
459667 : 157,
522298 : 72,
349869 : 154,
774447 : 88,
778984 : 163,
687969 : 93,
171503 : 272,
493915 : 90,
953998 : 308,
677791 : 248,
682877 : 93,
566442 : 54,
165664 : 60,
367828 : 180,
956331 : 202,
446707 : 95,
674521 : 186,
771530 : 101,
507370 : 227,
418106 : 56}

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

    
# ------------
# collatz_is_odd
# ------------

def collatz_is_odd(n) :

    if n & 1 == 1 :
        return True
    else :
        return False

# ------------
# collatz_cycle
# ------------

def collatz_cycle (n) :
    global cache
    assert n > 0
    if n == 1 :
        return 1
        
    elif collatz_is_odd(n) :
        if n not in cache :
            cache[n] = 2 + collatz_cycle(n + (n >> 1) + 1)
        return cache[n]
    else :
        if n not in cache :
            cache[n] = 1 + collatz_cycle(n >> 1)
        return cache[n] 

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    if i > j :
       temp = i
       i = j
       j = temp
       
    if( i <= (j >>1)) :
        i = j >> 1
    
    current = i
    while current <= j :

        temp_v = collatz_cycle(current)
        assert temp_v > 0
        if  current == i :
            v = temp_v
        elif temp_v > v : # Should I put an assert here?
            v = temp_v
            
        current = current + 1
    
    assert v > 0
    return v

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

# -------
# imports
# -------

import sys

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
