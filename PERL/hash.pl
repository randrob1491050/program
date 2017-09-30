#!perl

for($i=1;$i<=10;$i++)
{
    last if ($i==5); 
    print "$i\n";

}

for ($i=0;$i<=10;$i++)
{
		next if ($i%2 == 0);
		print "$i ÊÇÆæÊý\n";
}
