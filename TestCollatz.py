#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing & Raul B. Barbosa
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_is_odd, collatz_cycle

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :

    # ----
    # read
    # ----
    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        
    def test_read_2(self) :
        r = StringIO.StringIO("5 50\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] == 50)
        
    def test_read_3(self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    def test_read_4(self) :
        r = StringIO.StringIO("10002 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10002)
        self.assert_(a[1] == 2)
        
    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print_1(self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2(self) :
        w = StringIO.StringIO()
        collatz_print(w, 4, 1000, 220)
        self.assert_(w.getvalue() == "4 1000 220\n")
    
    def test_print_3(self) :
        w = StringIO.StringIO()
        collatz_print(w, 67, 994, 2323)
        self.assert_(w.getvalue() == "67 994 2323\n")
        
    def test_print_4(self) :
        w = StringIO.StringIO()
        collatz_print(w, 455, 1, 2022)
        self.assert_(w.getvalue() == "455 1 2022\n")        
    
    # -----
    # cycle
    # -----

    def test_cycle_1 (self) :
        v = collatz_cycle(1)
        self.assert_(v == 1)
        
    def test_cycle_2 (self) :
        v = collatz_cycle(3)
        self.assert_(v == 8) 

 
    # -----
    # is_odd
    # -----

    def test_is_odd_1 (self) :
        v = collatz_is_odd(5)
        self.assert_(v == True)
    
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
