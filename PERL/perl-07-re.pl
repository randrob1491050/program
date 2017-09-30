#!perl -w
print "#part 1\n";
my $some_other = "i dream of betty rubble.";
if ($some_other =~ /\brub/) {
	print "Aye, there's the rub.\n";
	}

print "#part 2\n";
print "Do You like Perl?(yes/no)";
my $like_perl = (<STDIN> =~ /\byes\b/i );
if ($like_perl) {
	print "You Result is: YES!\n";
} else {
		print "You Result is: NO!\n";
}

print "#part 3\n";
$_ = "Hello there, neighbor";
if (/\s(\w+), /) {
	print "the word was $1\n";
	print "That was ($`)($&)($').\n";
}
if (/(\S+) (\S+), (\S+)/) {
	print "the word was $1 $2 $3\n";
}

print "#part 4\n";
my @a = qw/2 4 6 8 10 12/;
my $x = join ":", @a;
print "$x\n";
my $b = "2:4:6:8:10:12";
my @y = split /:/, $b;
print "@y\n";
my $z = join "-", @y;
print "$z\n";

print "#part 5\n";
my $text = "Fred dropped a 5 ton granite block on Mr. Slate";
my @word = ($text =~ /([a-z]+)/ig);
print "Result is @word\n";

my $data = "Barney Rubble Fred Flintstone Wilma Flintstone";
my %last_name = ($data =~ /(\w+)\s+(\w+)/g);
my @k = keys %last_name;
my @v = values %last_name;
print "Keys is @k\n";
print "Values is @v\n";





