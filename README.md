# DFA

This program simulates a deterministic finite automaton. Given the state table of a DFA and a string, it decides whether this string is accepted by the automaton. Sample transcripts can be found below. 


Example 1:
>>> G = getDFA()
State names: a b c d e f g 
Alphabet: 0 1
Enter transition table:
   0 1 
a: b d 
b: c e 
c: b d
d: e f
e: e e
f: g d
g: f e
Start state: a
Final states: f
>>> simulate(G, '1100') True
>>> simulate(G, '0101') False
>>> simulate(G, '001100') True
>>> simulate(G, '0000') False
>>> simulate(G, '1111') True


Example 2:
>>> F = getDFA() 
State names: p q r 
Alphabet: 0 1
Enter transition table:
   0 1 
p: p q
q: r p
r: q r
Start state: p 
Final states: p
>>> simulate(F, '1001') True
>>> simulate(F, '1000') False
>>> simulate(F, '10010') True
>>> simulate(F, '11111') False
>>> simulate(F, '1111') True
>>> simulate(F, '1111000') True


Example 3:
>>> k = getDFA() 
State names: s i m o n 
Alphabet: 0 1
Enter transition table:
   0 1 
s: i m
i: o n
m: s i
o: o n
n: i s
Start state: s
Final states: m 
>>> simulate(k, '0') False
>>> simulate(k, '1') True
>>> simulate(k, '1001') False
>>> simulate(k, '1101') False
>>> simulate(k, '1111') False
>>> simulate(k, '1011') False
>>> simulate(k, '00000001') False
>>> simulate(k, '0111') True
