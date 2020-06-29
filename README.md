# This is a quick script that models interracial interactions in an unspecific population

## tldr; Even in a society where the likelihood of a negative interracial experience is relatively low, there will inevitably be a discrepancy in the rates at which different races experience negative interactions.

If we assume that in a society where the average incidence of negative interracial interactions is a
constant 0.1%:

Running the script as is returns:
```
Race.A
total people: 22800
average interactions: 360.0057894736842
average bad interactions: 0.008859649122807017
average good interactions: 359.9969298245614
average r_score: 0.00010000000000001697
----------------------------------------------------------------------------------------------------
Race.B
total people: 3900
average interactions: 359.75615384615384
average bad interactions: 0.03230769230769231
average good interactions: 359.7238461538462
average r_score: 9.999999999999317e-05
----------------------------------------------------------------------------------------------------
Race.C
total people: 3300
average interactions: 360.2481818181818
average bad interactions: 0.024242424242424242
average good interactions: 360.2239393939394
average r_score: 9.999999999999393e-05
```
Thus, minorities inevitably experience negative interracial experiences at about 3 times the rate
that the majority experiences it at.

---

If we then also assume that:
- Causing someone else to have a negative interaction makes them more likely to then initiate a
    negative interracial interaction
- Causing someone else to have a positive interaction makes them less likely to then initiate a
    negative interracial interaction
- Interacting with your own race makes you only a little more likely to initiate a negative
    interracial interaction

When we set ECHO_CHAMBER to true, we then get
```
Race.A
total people: 22800
average interactions: 359.9483333333333
average bad interactions: 0.002807017543859649
average good interactions: 359.9455263157895
average r_score: 5.5382964336921784e-05
----------------------------------------------------------------------------------------------------
Race.B
total people: 3900
average interactions: 359.8825641025641
average bad interactions: 0.02128205128205128
average good interactions: 359.86128205128205
average r_score: 4.554799402625675e-06
----------------------------------------------------------------------------------------------------
Race.C
total people: 3300
average interactions: 360.4957575757576
average bad interactions: 0.020303030303030302
average good interactions: 360.47545454545457
average r_score: 4.176065186636649e-06
----------------------------------------------------------------------------------------------------
```

The rate at which everyone experiences negative interactions actually falls, but the rate at which
minorities experience negative interactions compared to the majority actually increases to about 6
times.
