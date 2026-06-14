from engine.inputs import random_int


def check(T):
    T.eq(T.attr(T.make("BankAccount"), "balance"), 0,
         because="BankAccount() defaults to a balance of 0.")

    acc = T.make("BankAccount", 100)
    T.method(acc, "deposit", 50)
    T.eq(T.attr(acc, "balance"), 150, because="100 + 50 = 150.")
    T.eq(T.method(acc, "withdraw", 70), True,
         because="Enough funds -> withdraw returns True.")
    T.eq(T.attr(acc, "balance"), 80, because="150 - 70 = 80.")
    T.eq(T.method(acc, "withdraw", 999), False,
         because="Overdraw -> withdraw returns False.")
    T.eq(T.attr(acc, "balance"), 80,
         because="A refused withdrawal must leave the balance unchanged.")

    # withdrawing exactly the balance is allowed
    acc = T.make("BankAccount", 40)
    T.eq(T.method(acc, "withdraw", 40), True,
         because="Withdrawing the whole balance is allowed.")
    T.eq(T.attr(acc, "balance"), 0)

    # randomized sequence of operations
    for _ in range(6):
        bal = random_int(0, 100)
        acc = T.make("BankAccount", bal)
        for _ in range(8):
            amt = random_int(1, 60)
            if random_int(0, 1):
                T.method(acc, "deposit", amt)
                bal += amt
            else:
                ok = T.method(acc, "withdraw", amt)
                if amt <= bal:
                    T.eq(ok, True, because="withdraw %d from %d succeeds."
                                           % (amt, bal))
                    bal -= amt
                else:
                    T.eq(ok, False, because="withdraw %d from %d is refused."
                                            % (amt, bal))
            T.eq(T.attr(acc, "balance"), bal,
                 because="running balance should be %d." % bal)
    T.uses_class('BankAccount', because="The account is a `class` with state and methods.")
