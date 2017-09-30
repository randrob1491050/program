#!perl -w
print "#2 chapter\n";
my $radius = 12.5;
#chomp (my $radius = <STDIN>);
if ( $radius < 0 ) {
		print "Result is 0";
		exit;
	}
my $circ = $radius*(3.14*2);
print "Result is $circ\n";

chomp (my $input1 = <STDIN>);
chomp (my $input2 = <STDIN>);
my $sum = $input1 * $input2;
print "$sum\n";

print "Pls frist input character string:";
my $input3 = <STDIN>;
print "Pls second input number string:";
chomp (my $input4 = <STDIN>);
my $result = $input3 x $input4;
print "Result is: \n$result";