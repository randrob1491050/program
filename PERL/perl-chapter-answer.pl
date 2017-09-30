#!perl -w
print "#7 chapter\n";
my %last_name=(
  "fred" => "flintstone",
  "dino" => undef,
  "barney" => "rubble"
  );
  
foreach $person (qw<barney fred>){
print "I've heard of $person $last_name{$person}.\n";
}

my $x = join ":" , 4, 6, 8, 10, 12;
print "$x\n";

$string = "4:6:8:10:12";
@y = split /:/, $string;
print "@y\n";

$string = "4x6x8x10x12";
@z = split /x/, $string;
print "@z\n";