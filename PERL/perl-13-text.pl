#!perl -w
print "#part 1\n";
my $stuff = "Howdy world\n";
my $where1 = index($stuff, "w");
my $where2 = index($stuff, "w", $where1+1);
my $where3 = index($stuff, "w", $where2+1);
print "$where1\n";
print "$where2\n";
print "$where3\n";

print "#part 2\n";
my $where = substr("zong hua ren ming gong he guo", 9, 3);
print "$where\n";

print "#part 3\n";
my $long = "some very very long string";
my $find = substr( $long, index($long, "l") );
print "Result is: $find\n";

print "#part 4\n";
my $string1 = "Hello World";
substr($string1, 0, 5) = "Goodbye";
print "STRING 1: $string1\n";
my $string2 = "Hello World";
print "STRING 2: $string2\n" if ( $string2 =~ s/Hello/Goodbye/ );
#my $word = $string3 = "Hello World";
#$word =~ s/Hello/Goodbye/ ;
#print "STRING 3: $word\n";
my $string4 = "Hello World";
($word1 = $string4) =~ s/Hello/Goodbye/ ;
print "STRING 4: $word1\n";
print "STRING 4: $string4\n";

print "#part 5\n";
my %score = (
	"barney" => 195, 
	"fred" => 205,
	"dino" => 30,
	"bamm-bamm" => 195
	);
my @winners = sort by_score keys %score;
sub by_score {
	$score{$b} <=> $score{$a}
	or
	$a cmp $b
};
print "@winners\n";


