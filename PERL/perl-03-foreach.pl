#!perl -w
@rocks = qw / bedrock slate lava /;
foreach $rock (@rocks)	{
	$rock = "\t$rock";
	$rock .= "\n";
}
	
print "The rocks are: \n", @rocks;


foreach $rock (qw/bedrock slate lava/) {
	print "One rock is $rock.\n";
}
