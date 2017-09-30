#!/usr/bin/perl

use warnings;
use strict;
use Term::ReadKey;
use WWW::Mechanize;

#die "just input your name. then i will ask for your pin...^-^\n" if (@ARGV > 1);
my $usr = "wangdy";
#	or die "must input your name!\n";
#print "Pls input your pin to get the dynamic pass!\n";
#ReadMode('noecho');ff
#chomp ( my $pin = <STDIN> );
my $pin = "5151" ;
#ReadMode('restore');

my %submitHash;
my $uri = "http://114.80.88.25/p.php";

my $mech = WWW::Mechanize->new();

if (!defined $usr or !defined $pin) {
	die("You must pass through basic Auth!.\n");
}else{
    	$mech->credentials('51.com','www.51.com');
	my $response = $mech->get( $uri );
	$response->is_success or die "Can't fetch $uri\n", $response->status_line, "\n";
}

my $formList = $mech->forms();
my $form;
my @field;
foreach (@$formList){
	$form = $_->dump;
}
push @field,split '\n',$form;
map { if (/token|time/) { $submitHash{$1}=$2 if /\s+(.*)=(.*?)\s+\(/}} @field;
$submitHash{'usr'} = $usr;
$submitHash{'pin'} = $pin;

$mech->submit_form(with_fields => \%submitHash); #这里已经提交了表单,因此用不到下面的mech->submit方法
#$mech->submit;
my $rep = $mech->content;
my $dynamic = $1 if $rep =~ /center.*(?<=is )(.*)(?=\<\/h1)/;
print $dynamic."\n";