#!perl -w
print "#part 1\n";
$family_name{"fred"} = "flintstone";
$family_name{"barney"} = "rubble";

foreach $person (qw< barney fred >) {
	print "I've heard of $person $family_name{$person}.\n";
}


print "#part 2\n";
%some_hash = ("foo",35,"bar",12.4,2.5,"hello","wilma",1.72e30,"betty","bye\n");
@any_array = %some_hash ;
print "@any_array\n";


print "#part 3\n";
my %last_name = (
	"fred" => "flintstone",
#	"dino" => undef,
	"barney" => "rubble",
	"betty" => "rubble",
	);
@any_name = %last_name ;
print "@any_name\n";


print "#part 4\n";
my @k = keys %last_name;
my @v = values %last_name;
my $count = keys %last_name;

print "result is @k\n";
print "result is @v\n";
print "result is $count\n";

print "#part 5\n";
my %hash = ("a" => 1, "b" => 2, "c" => 3);
while ( ( $k , $v) = each %hash ) {
	print "$k result just $v\n";
}

print "#part 6\n";
@s = (sort keys %hash);
print "@s\n";
foreach $key (sort keys %hash) {
	$value = $hash{$key};
	print "$key result just $value\n";
}


print "#6 chapter\n";
#my %last_name = (
#	fred => "flintstone",
#	barney => "rubble",
#	wilma => "flintstone",
#);

#print "Pls inpout string with 'fred' 'barney' 'wilma': ";
#chomp (my $input = <STDIN>);
#print $last_name{$input};
	
#my (@words, %count, $word);
#chomp (my @words = <STDIN>);
#foreach $word (@words) {
#	$count{$word} += 1;
#}
#foreach $word (sort keys %count) {
#	print "The $word just seen $count{$word} \n";
#}
