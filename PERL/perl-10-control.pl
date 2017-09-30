#!perl
#print "#part 1\n";
$_ = 0;
print " ", ($_ += 2) while $_ < 10;
print "\n";

#print "#part 2\n";
my @people = qw{ fred barney fred wilma dino barney fred pebbles };
my %count;
$count{$_}++ foreach @people;
#my @k = keys %count;
#my @v = values %count;
while ( ( $k, $v ) = each %count ) {
	print "$k\t\t$v\n";
}

#print "#part 3\n";
my @peoples = qw{ fred barney bamm-bamm wilma dino barney betty pebbles };
my %seen;
foreach (@peoples) {
	if ( $seen{$_}++ ) {
		print "I've seen you somewhere before, $_ !\n"
	}
}
for ( $i=-5; $i<=10; $i+=3 ) {
	print "Result is: $i!\t";
}
print "\n";

#print "#part 4\n";
my @text = qw/111 222 333/;
my $errors = 0;

foreach ( @text ) {
	print "Type the word '$_': ";
	chomp (my $try = <STDIN> );
	if ( $try ne $_ ) {
		print "Sorry - '$try' not right.\n\n";
		$errors++;
		redo;
	}
}
print "you with $errors errors.\n";

print "#part 5\n";
foreach (1..10) {
	print "Iteration number $_.\n\n";
	print "Please choose: last, next, redo, or none of the above?";
	chomp ( my $choice = <STDIN> );
	print "\n";
	last if $choice =~ /last/i;
	next if $choice =~ /next/i;
	redo if $choice =~ /redo/i;
	print "That wasn't any of the choices ... onward!\n\n";
}
print "that's all,folks!\n";

print "#part 6\n";
chomp (my $width = <STDIN>);
print "$width\n"; 
  ($width < 10) ? print "small\n" :
	($width < 20) ? print "medium\n" : 
	($width < 30) ? print "large\n" :
								  print "extra-large\n";
								  
								  
								  
								  
								  