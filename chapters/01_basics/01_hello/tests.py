def check(T):
    out = T.run()
    T.eq(out, "Hello, output",
         because="Your program should print exactly: Hello, output")
    T.uses_print(because="Use print() to put the text on the screen.")
