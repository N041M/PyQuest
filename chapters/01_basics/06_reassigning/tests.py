def check(T):
    out = T.run()
    T.eq(out, "10\n20",
         because="Print the variable (10), reassign it to 20, then print again.")
    T.reassigns_a_variable(values=(10, 20),
        because="Assign 10, then reassign the SAME variable to 20 -- don't "
                "use two different names.")
    T.prints_name(min_calls=2, same=True,
        because="Both lines must come from printing the variable -- not the "
                "numbers 10 and 20 typed in.")
