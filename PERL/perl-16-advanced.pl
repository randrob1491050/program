#!perl -w
print "#part 1\n";
sub big_money {
		my $number = sprintf "%.2f", shift @_;
		1 while $number =~ s/^(-?\d+)(\d\d\d)/$1,$2/;
		$number =~ s/^(-?)/\$/;
		$number;
	}	
my @data = (4.75, 1.5, 2, 1234, 6.9456, 12345678.9, 29.95);
my @formatted_data;
foreach (@data) {
	push @formatted_data, &big_money($_);
}
print "@formatted_data\n";

print "#part 2\n";
my @newformatted_data = map { &big_money($_) } @data;
print "@newformatted_data\n";

print "#part 3\n";
#@ARGV = qw# C:\Documents and Settings\Administrator\×ÀÃæ\perl\222.txt #;
open FILE, 'C:\Documents and Settings\Administrator\×ÀÃæ\perl\222.txt' 
	or die "($!) is wrong\n";

while (<FILE>) {
	chomp;
	my @item = split /:/;
	my($two, $five) = ($item[2], $item[5]);
	print "2row Result is $two, 5row Result is $five\n";
}
print "\n";

open FILE, 'C:\Documents and Settings\Administrator\×ÀÃæ\perl\222.txt' 
	or die "($!) is wrong\n";
while (<FILE>) {
		chomp;
		my $one = (split /:/)[1];
		my $five = (split /:/)[5];
		print "1row Result is $one, 5row Result is $five\n";
}



