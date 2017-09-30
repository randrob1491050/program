#!perl -w
print "#part 1\n";
my $timestamp = 1180630098;
my $date = localtime $timestamp;
my $now = time;
my $dates = localtime $now;
my $nows = gmtime;
print "'date' Result is: $date\n";
print "'now' Result is: $now\n";
print "'dates' Result is: $dates\n";
print "'nows' Result is: $nows\n";
print ( my $time = localtime time );



