#!perl -w
print "#4 chapter\n";
#my @fred = qw/1 3 5 7 9/;
#my $free_total = &total(@fred);
#print "The total of \@fred is $free_total .\n";
#print "Enter some number on separate lines: ";
#my $user_total = &total(<STDIN>);
#print "The total of those number is $user_total .\n";

my @new_total = &total(@1..1000);
print "Result is: @new_total\n";

sub total {
	my $sum = 0;
	foreach (@_) {
		$sum += $_;
	}
	$sum;
}

sub average {
	$count = @_;
	$sum = &total(@_);
	$sum/$count;
}

sub above_average {
	$average = &average(@_);
	my @list;
	foreach $element (@_) {
		if ( $element > $average ) {
			push @list, $element;
		}
	}
	@list;
}

my @fred = &above_average(1..10);
print "\@fred is @fred\n";
print "(Should be 6 7 8 9 10)\n";
my @barney = &above_average(100, 1..10);
print "\@barney is @barney\n";
print "(Should be just 100)\n";