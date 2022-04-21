// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(FOREVER)

    // if R[KBD] == 0 then val=0 else val = -1
    @KBD
    D=M
    @if
    D;JEQ

    @val
    M=-1
    @else
    0;JMP

    (if)
        @val
        M=0
    
    (else)

    @i
    M=0     // i = 0
    @SCREEN
    D=A
    @pointer
    M=D     // pointer = SCREEN

    (LOOP)
        // if i == 8192 goto STOP
        @i
        D=M
        @8192
        D=D-A
        @STOP
        D;JEQ

        // RAM[pointer] = val
        @val
        D=M
        @pointer
        A=M
        M=D

        // pointer++, i++
        @pointer
        M=M+1
        @i
        M=M+1

        @LOOP
        0;JMP
    
    (STOP)
        @FOREVER
        0;JMP
