#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing & Raul B. Barbosa
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {1:1}

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
