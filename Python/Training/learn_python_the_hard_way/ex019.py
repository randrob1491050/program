#!python

def coins_and_boxs(coin_count, box_count):
    print "coins amount is %d" % coin_count
    print "boxs amount is %d" % box_count
    print "and coins plus boxs amount is %d\n" % (coin_count + box_count)

coins_and_boxs(10, 20)

new_coin_count = 30
new_box_count = 15

coins_and_boxs(new_coin_count, new_box_count)

coins_and_boxs(new_coin_count+11,new_box_count+22)

print "please input coin and box number"
in_coin_count = int(raw_input("Input Coin Number:"))
in_box_count = int(raw_input("Input Box Number:"))

coins_and_boxs(in_coin_count, in_box_count)

