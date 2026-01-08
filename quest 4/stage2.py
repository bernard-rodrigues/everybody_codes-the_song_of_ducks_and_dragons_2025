gears_list = f"""939
917
911
898
895
887
882
879
873
859
843
822
816
806
784
755
746
735
725
696
693
664
652
643
629
617
592
588
585
575
561
551
529
522
521
493
492
477
456
431
408
391
367
363
357
351
327
312
294
253""".split("\n")

converted_gears_list = [int(i) for i in gears_list]

turns = 10000000000000

for i in range(len(converted_gears_list) - 1):
    # Now we're working backwards
    gear_index = len(converted_gears_list) - i - 1
    # The number of turns of the last gear must be multiplied by the ratio gear_current/gear_previous. Current from the last to the second.
    turns *= converted_gears_list[gear_index]/converted_gears_list[gear_index-1]

print(round(turns))