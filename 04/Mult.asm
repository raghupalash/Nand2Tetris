// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// m0 = R0
@R0
D=M
@m0
M=D

//m1 = R1
@R1
D=M
@m1
M=D

// prod = 0
@prod
M=0
// R2 = 0
@R2
M=0

// i = 0
@i
M=0

(LOOP)
    // if i == m1, then goto STOP
    @i
    D = M
    @m1
    D = D - M 
    @STOP
    D;JEQ

    // prod = prod + m0
    @m0
    D=M
    @prod
    M=M+D

    // i ++
    @i
    M=M+1

    @LOOP
    0;JMP

(STOP)
    @prod
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP