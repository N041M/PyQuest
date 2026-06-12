def check(T):
    out = T.run()
    T.eq(out, "Visible",
         because="Only 'Visible' should print -- the 'Hidden' line must not run.")
    src = T.source()
    # the actual print statement (commented or not) -- not prose that merely
    # mentions the word "Hidden" (e.g. the instructions in the file header).
    hidden = [ln for ln in src.splitlines()
              if "print(" in ln and "Hidden" in ln]
    T.true(len(hidden) > 0,
           because="Don't delete the print(\"Hidden\") line -- comment it out "
                   "with a # instead.")
    commented = all("#" in ln and ln.index("#") < ln.index("Hidden")
                    for ln in hidden)
    T.true(commented,
           because="Put a # in front of the print(\"Hidden\") line so it is "
                   "commented out, not running.")
