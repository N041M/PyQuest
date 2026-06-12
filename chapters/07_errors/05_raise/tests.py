from engine.inputs import random_int


def check(T):
    T.eq(T.call("checked_age", 30), 30)
    T.eq(T.call("checked_age", 0), 0,
         because="Zero is a valid age -- only negatives are senseless.")
    T.raises(ValueError, "checked_age", -1)
    T.raises(ValueError, "checked_age", -40)
    for _ in range(6):
        n = random_int(0, 120)
        T.eq(T.call("checked_age", n), n,
             because="A valid age comes back unchanged.")
        T.raises(ValueError, "checked_age", -random_int(1, 120))
    T.uses_raise(because="The lesson is raising your own error -- "
                         "raise ValueError(...) on bad input.")
