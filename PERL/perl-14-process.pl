#!perl -w
print "#part 1\n";
system "dir";
system 'dir c:';

chomp (my $ports = `netstat -na | find "7070"`);
print "Result is:\n $ports\n";

my @functions = qw{ int rand sleep length hex eof exit sqrt umask };
my %about;

foreach (@functions) {
	$about{$_} = `perldoc -t -f $_`;
}

print "%about\n";