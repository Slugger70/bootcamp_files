#!/usr/bin/env perl
use warnings;
use strict;

my $a = 111;
$a *= 80;
$a++;
$a*=250;
my $b = 2222;
$a += 2*$b;
$a-=250;
$a/=2;
print "$a\n";
