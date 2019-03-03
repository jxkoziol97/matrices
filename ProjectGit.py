#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Matrix(object):
    def __init__(self, L):
        self.a = L[0][0]
        self.b = L[0][1]
        self.c = L[1][0]
        self.d = L[1][1]
        
    def __str__(self):
        return "[%f,%f]\n[%f,%f]" % (self.a, self.b, self.c, self.d)
    
    def determinant(self):                                       #(a*d) - (d*c)
        Determinant = (self.a * self.d) - (self.b * self.c)
        return Determinant

    def trace(self):                                                      #a+d
        Trace = (self.a + self.d)
        return Trace
    
    def inverse(self):
        if self.determinant() == 0:
            return "Matrix is Singular"
        
        a = self.d/self.determinant()
        b = -self.b/self.determinant()
        c = -self.c/self.determinant()
        d = self.a/self.determinant()

        return "Inverse:\n[%f,%f]\n[%f,%f]" % (a, b, c, d)
    
    def matrix_product(self, Matrix2):
        Pa = self.a * Matrix2.a + self.b * Matrix2.c
        Pb = self.a * Matrix2.b + self.b * Matrix2.d
        Pc = self.c * Matrix2.a + self.d * Matrix2.c
        Pd = self.c * Matrix2.b + self.d * Matrix2.d
        
        return "Matrix 1 * Matrix 2:\n[%f,%f]\n[%f,%f]" % (Pa, Pb, Pc, Pd)
    
    def characteristic_polynomial(self):
        T = self.trace()
        D = self.determinant()
        
        CP = "(x^2) - (%f*x) + (%f)" % (T, D)
        return CP
    
def main():
    print("[a,b]\n[c,d]\n")
    print("Enter Values for Matrix 1:")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    M1 = Matrix([[a,b],[c,d]])
    print("\nMatrix 1:")
    print(M1)
    print("\nDeterminant:", M1.determinant())
    print("\nTrace:", M1.trace())
    print("\n", M1.inverse())
    print("\nCharacteristic Polynomial:")
    print(M1.characteristic_polynomial())
    print("\nEnter Values for Matrix 2:")
    e = float(input("Enter e: "))
    f = float(input("Enter f: "))
    g = float(input("Enter g: "))
    h = float(input("Enter h: "))
    M2 = Matrix([[e,f],[g,h]])
    print("\nMatrix 2:")
    print(M2)
    print("\n", M1.matrix_product(M2))
main()