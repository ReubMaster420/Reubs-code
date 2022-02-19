rider(A, B) :-				/* The Base Case */
parent(A, B).
rider(A, B) :-				/* The General Case */
parent(A, X),
rider(X, B).

parent(addn,reuben).
parent(reuben,chris).
