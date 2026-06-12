def check(T):
    out = T.run()
    T.eq(out, "42\n42",
         because="Expected 42 printed on two separate lines.")
    T.assigns_a_variable(because="Store 42 in a variable first.")
    T.prints_computed(
        min_calls=2,
        because="Print the variable TWICE -- two separate print() calls, "
                "not the number 42 typed in (and not one two-line string).")
