def check(T):
    out = T.run()
    T.eq(out, "10\n20",
         because="Print the variable (10), reassign it to 20, then print again.")
    T.reassigns_a_variable(
        because="Reassign the SAME variable from 10 to 20 -- don't use two "
                "different names.")
    T.prints_computed(
        because="Print the variable, not the numbers 10 and 20 directly.")
