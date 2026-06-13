def check(T):
    out = T.run()
    T.eq(out, "42\n42",
         because="Expected 42 printed on two separate lines.")
    T.assigns_a_variable(value=42,
        because="Store the NUMBER 42 in a variable first -- one assignment "
                "the rest of the program actually uses.")
    T.prints_name(min_calls=2, same=True,
        because="Print the SAME variable twice -- two separate print() calls "
                "showing it, not the number 42 typed in again.")
