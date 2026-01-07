gears_list = f"""598
589|589
587|587
572|572
562|562
556|556
541|541
532|532
522|1044
513|513
506|1518
505|505
494|1482
490|490
472|944
470|470
460|1840
449|449
436|436
435|435
430|1290
420|420
416|1248
401|401
391|1564
388|388
379|1516
367|367
352|1056
351|351
345|1380
337|337
332|664
328|328
326|652
325|325
309|618
301|301
282|564
267|267
260|520
251|251
234|468
230|230
215|860
211|211
192|576
188|188
176|528
147""".split("\n")

turns = 100

for i in range(len(gears_list) - 1):
    # Check if it is a double gear or not and store the value according with its position
    # Value at right if the gear is at left
    # Value at left if the gear is at right
    gear_one = int(gears_list[i].split("|")[1]) if gears_list[i].count("|") == 1 else int(gears_list[i])
    gear_two = int(gears_list[i+1].split("|")[0]) if gears_list[i+1].count("|") == 1 else int(gears_list[i+1])

    turns *= gear_one/gear_two

print(turns)