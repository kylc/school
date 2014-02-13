\ 1
." Hello world"
cr

\ 3
16 32 / 74 16 dup dup * * * + 5 10 mod + .
cr

\ 4
16e0 32e0 f/ 74e0 16e0 fdup fdup f* f* f* f+ 5 10 mod s>f f+ f.
cr

\ 5
16e0 32e0 f/ 74e0 16e0 fdup fdup f* f* f* f+ 5 10 mod s>f f+ f.
cr

\ 6
16 s>f 32e0 f/ 74e0 16 dup dup * * s>f f* f+ 5 10 mod s>f f+ f.
cr

\ 7
variable x
variable y
16 y !
32e0 x f!
y @ s>f x f@ f+ 3e0 6 s>f 10e0 f/ f* f- f.
cr

\ 8
: num8 5 3 < if 7 else 2 endif ;
num8 .
cr

\ 9
: num9 5 3 > if 7 else 2 endif ;
num9 .
cr

\ 10
: num10 6 0 ?do i . loop ;
num10
cr

\ 11
: convertint ( x -- x )
  s>f ;

\ 12
: fact ( n -- n! )
  dup 0 <= if
    drop
    1
  else
    dup 1- recurse *
  endif ;

\ 13
: fib ( i -- f )
  dup 0 = if drop 0 else
  dup 1 = if drop 1 else
    1- dup 1- recurse swap recurse +
  endif endif ;
