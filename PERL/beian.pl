#!/usr/bin/perl
use strict;
use utf8;
use Data::Dumper;

binmode(STDIN, ':encoding(utf8)');
binmode(STDOUT, ':encoding(utf8)');
binmode(STDERR, ':encoding(utf8)');
use Web::Scraper;
use URI;
my $domain="anjuke.com";

#foreach $domain (@ARGV){
my $uri = URI->new("http://www.beianchaxun.net/piliang/chaxun?domains=$domain");
my $scraper = scraper {
    process '//div[@id="show_table"]//table[@class="seo"]/tr/td[text()]','text[]'=>'TEXT';
};


my $result = ${$scraper->scrape($uri)}{'text'};


print Dumper @$result;
pop @$result;
print join "\t",@$result;
print "\n";
#}
