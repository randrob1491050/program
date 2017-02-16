#!/usr/bin/perl

use warnings;
use strict;
use Data::Dumper;
use Term::ReadKey;
use Storable;
use File::Basename;
use Encode qw/decode encode/;
use WWW::Mechanize::Firefox;
use Web::Scraper;
use utf8;

#binmode STDOUT,':utf8';

die "just input your name. then i will ask for your pass...^-^\n" if (@ARGV > 1);
my $usr =shift
        or die "must input your name!\n";
print "Pls input your pass!\n";
ReadMode('noecho');
chomp ( my $pass = <STDIN> );
ReadMode('restore');

my $dir = dirname($0);
my $blankDataFile = "$dir/blank_data.txt";
my %submitHash;								#用于提交 登陆界面的数据
my $url = "http://192.168.57.118/study";

# 连接对应的url并获取数据
$ENV{MOZREPL} = "127.0.0.1:4242";					#设置默认的连接firefox的ip以及相应的port
my $wmf = WWW::Mechanize::Firefox->new(
	agent => 'Mozilla/5.0',
	tab => qr/\W+/,
	create => 1,
	activate=>1,
	autoclose => 0,
);

$wmf->allow(
	javascript=>1,
	subframes=>1,
);						#设置javascript支持

$wmf->get($url,'no_cache'=>1);							#打开相应的url

my @field = split '\n',$wmf->content();

map { if (/formid/) { $submitHash{$1}=$2 if /\s+name=\"(.*)\"\s+value=\"(.*?)\"\s+.*/ }} @field;

$submitHash{'account'} = ($usr);
$submitHash{'password'} = $pass;
#$submitHash{'use_cookie'} = 'off';

$wmf->untick('use_cookie',undef,undef);
$wmf->submit_form(
	form_name => 'logonForm',
	with_fields => \%submitHash
); #这里已经提交了表单,因此用不到下面的wmf->submit方法

#$wmf->follow_link(tag_regex => qr/^(iframe|frame)$/ );
my $content = $wmf->content;
#$wmf->save_content('study3.txt');	# save the content of url,use to debug...

####
# write node
# <fieldset id="write_node">
####

# post 'make a copy' content

# 1.get the content of 'make a copy'
my $scraper = scraper {
	    process '//input[@id=~/content_a_\d/]','ans[]'=>'@value';
	    process '//input[@id=~/blank_key/]','blank_q_name[]'=>'@name';
    };
my $copy = ${$scraper->scrape($content)}{'ans'};

# 2.filling content
foreach (0..$#{$copy}) {
	my $sel = q(//textarea[@id="content_q_).($_+1).qq("]);
	my $xpath;
	eval { 
		$xpath = $wmf->xpath("$sel",one=>1);
	};
	if (! $@ ) {
#		sleep 120;
		$wmf->field($xpath,$copy->[$_]);
	}else{
		$sel = q(//input[@id="content_q_).($_+1).qq("]);
		$xpath = $wmf->xpath("$sel",one=>1);
#		sleep 120;
		$wmf->field($xpath,$copy->[$_]);
	}
}

# 3. submit 'make a copy'
# not finish...
#eval {
#	$wmf->click({xpath => q{//input[@value="抄写提交"]}});
#};

=pod
#foreach (@links){
#        my $uri = $_->url_abs();
#        print $uri,"\n";
#}
exit 12;

=cut

####
# blank node
# <fieldset id="blank_node">
####

my $blankDataRef = retrieve($blankDataFile);
my $blank_q = ${$scraper->scrape($content)}{'blank_q_name'};
foreach ( @$blank_q ) {
	my $path = $wmf->xpath("//input[\@id='$_']",one=>1);
	if (exists $blankDataRef->{$_}){
#		sleep 180;
		$wmf->field($path,decode("utf8",$blankDataRef->{$_}));
	}

}

#eval {
#	$wmf->click({xpath => q{//input[@value="填空提交"]}});
#};
####
# feeling node
# <div id="feeling_node">
####

# not finish
#my $feel = "learning...";
# set xpath
#my $ready_to_fill = $wmf->xpath('//textarea[@id="feel_keys_1"]',one=>1);
#my $ready_to_fill = $wmf->xpath('/html/body[@class="wysiwyg"]',one=>1);
#my $ready_to_fill = $wmf->xpath('//iframe[@id="feel_buxie_1-wysiwyg-iframe"]',one=>1);
#my $ready_to_fill = $wmf->xpath('//textarea[@id="feel_keys_1"]',one=>1);
# filling...
#my $ready_to_fill = $wmf->xpath('//body[@class="wysiwyg"]',one=>1);
#$wmf->field($ready_to_fill,$feel);
