def check(T):
    out = T.run()
    T.eq(out, "2024-12-25",
         because="Expected the three numbers 2024, 12, 25 joined by dashes.")
    T.print_uses_keyword("sep",
        because="Join them with the sep setting: print(2024, 12, 25, sep='-') "
                "-- don't type the dashes into one string yourself.")
