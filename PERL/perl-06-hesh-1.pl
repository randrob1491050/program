#/bin/perl -w
my %hash = (
      John => "1982.1.5",
      Paul => "1978.11.3",
      Lee => "1976.3.2",
      Mary => "1980.6.23",
      Kayle => "1984.6.12",
      Ray => "1978.5.29",
    );

while ( my @pepole = each %hash ) {
    print "@pepole\n";
  }

while (($key, $value) = each %hash) {
    print  "Bingo: $key, $value\n" if ($value gt "1980");
  }