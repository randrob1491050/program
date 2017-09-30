#!perl -w

@rocks = qw/ bedrock slate rubble granite /;
@sorted = sort(@rocks);
print "\@sorted is @sorted.\n";

@back = reverse sort @rocks;
print "\@back is @back.\n";

@rocks = sort @rocks;
print "\@rocks is @rocks.\n";

@numbers = sort 97..102;
foreach $number (@numbers) {
	$number = "\t$number";
	$number .= "\n";
}
print "\@numbers is \n" ,@numbers;

print "#3 chapter\n";
#print "#reverse method 1\n";
print "Pls input some lines,press Ctrl-Z:\n";
#my @lines = <STDIN>;
#my @reverse_lines = reverse @lines;
#print "@reverse_lines\n";
print "#reverse method 2\n";
print "Pls input some lines,press Ctrl-Z:\n";
#print reverse <STDIN>;

#my @array_sample = qw/fred betty barney dino wilma pebbles bamm-bamm/;
#while (<STDIN>) {
#	print "Result is: $array_sample[ $_ - 1 ]\n";
#}

print "#sort method 1\n";
#chomp (my @lines = <STDIN>);
#my @sorted = sort @lines;
#print "@sorted\n";
print "#sort method 2\n";
print sort <STDIN>;