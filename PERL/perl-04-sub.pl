#!perl -w
#part 1
sub min {
	my ($min_far) = shift @_;
	foreach (@_) {
		if ($_ < $min_far) {
			$min_far = $_;
		}
	}
	$min_far;
}

$minimum = &min(34,23,64,6);

print "this rusult: $minimum\n";

#part 2
foreach (20..25) {
	my ($result) = $_ * $_;
	print "$_ square is $result\n";
}

#part 3
use strict;
my @names = qw/fred barney betty dino wilma pebbles bamm-bamm/;
my $result = &find( "wilma",@names );

sub find {
	my ( $what,@list ) = @_;
	foreach (0..$#list) {
		if ( $what eq $list[$_] ) {
			return $_;
		}
		-1;
	}
}

print "result is $result\n";

#part 4
use strict;
my $min = 12;
my $max = 20;

my @result = &sequen ;

sub sequen {
	if ( $min < $ max ) {
		$min..$max;
	} else {
		reverse $max..$min;
	}
}

print "result is @result\n";





