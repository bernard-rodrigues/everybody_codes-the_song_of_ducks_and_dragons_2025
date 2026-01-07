gears_list = f"""1000
997
972
947
930
906
879
851
826
811
799
775
763
745
727
715
688
671
649
624
595
576
548
544
529
525
523
514
502
481
454
427
400
379
351
332
322
304
287
269
256
229
222
204
178
155
142
134
120
108""".split("\n")

converted_gears_tuple = (int(i) for i in gears_list)

turns = 2025

for i in range(len(converted_gears_tuple) - 1):
    # The number of turns of the first gear must be multiplied by the ratio gear_current/gear_next. Current from the first to the penultimate.
    turns *= converted_gears_tuple[i]/converted_gears_tuple[i+1]

print(round(turns))