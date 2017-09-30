#!python

formatter = "%r %r %r %r"

#Print 1 2 3 4
print formatter % (1, 2, 3, 4)
#Print one two three four
print formatter % ("one", "two", "three", "four")
print formatter % ('one', 'two', 'three', 'four')
#Print True False False True
print formatter % (True, False, False, True)
#Print '%r %r %r %r' * 4
print formatter % (formatter, formatter, formatter, formatter)
#Print strings strings strings strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter * 4
print "#####" * 4
