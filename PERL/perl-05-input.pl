#!perl -w

@ARGV = qw# c:\Perl\bin\111.txt #;

while (<>) {
	chomp;
	print "result is $_\n";
}

chomp (@array = qw/123 234 345/);
print @array, "\n";
print "@array\n";

$result = print("hello world!\n");
print "reslut is $result\n";

print ((2+3)*4);
print "\n";

my $user =  "merlyn";
my $days = 20090829;

printf "Hello,%s;your password expires in %d days!\n", $user, $days;

printf "%10s\n", "merlyn";
printf "%5d\n", 42;

my @items = qw/wilma dino pebbles/;
printf "The items are: \n".("%10s\n" x @items), @items;
#printf "The items are: \n".("%10s\n" x ($number = @items)), @items;


print "#5 chapter\n";
#chomp (my @file = <>);
#my @sort = reverse @file;
#foreach (@sort) {
#	print "$_\n";
#}

#chomp (my @input = <STDIN>);
#print "1234567890" x 7, "12345\n";
#foreach (@input) {
#	printf "%20s\n", $_;
#}

print "Pls input width number: ";
chomp (my $width = <STDIN>);
print "Pls input some string: \n";
chomp (my @input = <STDIN>);
print "1234567890" x (($width+9)/10), "\n";
foreach (@input) {
	printf "%${width}s\n", $_;
}
