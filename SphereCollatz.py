#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing & Raul B. Barbosa
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {837799 : 525,
626331 : 509,
939497 : 507,
704623 : 504,
927003 : 476,
910107 : 476,
511935 : 470,
767903 : 468,
796095 : 468,
970599 : 458,
546681 : 452,
820023 : 450,
818943 : 450,
820022 : 450,
410011 : 449,
615017 : 447,
922525 : 445,
922526 : 445,
886953 : 445,
922524 : 445,
906175 : 445,
938143 : 445,
461262 : 444,
461263 : 444,
230631 : 443,
665215 : 442,
691895 : 442,
691894 : 442,
345947 : 441,
997823 : 440,
518921 : 439,
792735 : 437,
775035 : 437,
778382 : 437,
778383 : 437,
389191 : 436,
583787 : 434,
875681 : 432,
919791 : 432,
871915 : 432,
656761 : 429,
985143 : 427,
980905 : 427,
985142 : 427,
492571 : 426,
502137 : 426,
753206 : 424,
739143 : 424,
738857 : 424,
753207 : 424,
735679 : 424,
376603 : 423,
554143 : 421,
564905 : 421,
827503 : 419,
847358 : 419,
854191 : 419,
831215 : 419,
847359 : 419,
423679 : 418,
635519 : 416,
640641 : 416,
642075 : 416,
960962 : 414,
952479 : 414,
960963 : 414,
953279 : 414,
935479 : 414,
934299 : 414,
950943 : 414,
935478 : 414,
963113 : 414,
467739 : 413,
480481 : 413,
722335 : 411,
712683 : 411,
720723 : 411,
701607 : 411,
701609 : 411,
720722 : 411,
360361 : 410,
526207 : 408,
526206 : 408,
540542 : 408,
525543 : 408,
540543 : 408,
270271 : 407,
263103 : 407,
810814 : 406,
801769 : 406,
789310 : 406,
788315 : 406,
789311 : 406,
810399 : 406,
810815 : 406,
807327 : 406,
405407 : 405,
394655 : 405,
608111 : 403,
601327 : 403,
591983 : 403,
900735 : 401,
901991 : 401,
845223 : 401,
912511 : 401,
877399 : 401,
886855 : 401,
912167 : 401,
877398 : 401,
887975 : 401,
438699 : 400,
658049 : 398,
686985 : 398,
665979 : 398,
987074 : 396,
987075 : 396,
987081 : 396,
999295 : 396,
999294 : 396,
998969 : 396,
499647 : 395,
493537 : 395,
515239 : 395,
777327 : 393,
740307 : 393,
772859 : 393,
740310 : 393,
740311 : 393,
749471 : 393,
749227 : 393,
801147 : 393,
769641 : 393,
769305 : 393,
740306 : 393,
370153 : 392,
370155 : 392,
577230 : 390,
577231 : 390,
555233 : 390,
555231 : 390,
576978 : 390,
576979 : 390,
555230 : 390,
288615 : 389,
288489 : 389,
277615 : 389,
865469 : 388,
865401 : 388,
810603 : 388,
874494 : 388}

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
