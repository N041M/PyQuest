def check(T):
    out = T.run()
    T.eq(out, "Counting:\n1 2 3",
         because="Expected two lines: 'Counting:' then the numbers 1 2 3.")
    T.print_has_min_args(3,
        because="Print the numbers as separate values: print(1, 2, 3) -- "
                "don't type \"1 2 3\" as one string.")
