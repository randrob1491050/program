#!/bin/sh

origin_url="https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf"
origin_file="accelerated-domains.china.conf"
filter_file="china_domain_list"
pac_file="china_domain_pac"

if [ ! -e $origin_file ]; then
    wget $origin_url
    cat $origin_file | cut -d'/' -f2 > $filter_file
    sed -e 's/^/        shExpMatch\(host\,\"*\./g' $filter_file | sed -e 's/$/\"\) \|\|/g' > $pac_file
else
    cat $origin_file | cut -d'/' -f2 > $filter_file
    sed -e 's/^/        shExpMatch\(host\,\"*\./g' $filter_file | sed -e 's/$/\"\) \|\|/g' > $pac_file
fi

if [ $? = 0 ]; then
    echo "pac_file has created"
else
    echo "having some problem,check it"
fi
