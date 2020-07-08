#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os, sys, json
import requests
from optparse import OptionParser

def print_color(color,text):
    print("\033[1;{0}m{1}\033[0m".format(color,text))

if __name__ == "__main__":
    usage='''
        ./get_config.py --e pro --a qa -n backoffice
        ./get_config.py --e pro --a qa -n backoffice -g test1
        '''.format(sys.argv[0])
        
    parser = OptionParser(usage=usage)
    parser.add_option("-e","--env"      , dest="env"        , default=None)
    parser.add_option("-a","--appid"    , dest="appid"      , default=None)
    parser.add_option("-n","--namespace", dest="namespace"  , default='application')
    parser.add_option("-g","--cluster"  , dest="cluster"    , default='default')
    (options, args) = parser.parse_args()

    #config
    env        = options.env
    appid      = options.appid
    namespace  = options.namespace
    cluster    = options.cluster
    
    # Get meta Url
    dev_meta ='http://apollo-dev.shub.us'
    fat_meta ='http://apollo-fat.shub.us'
    uat_meta ='http://apollo-uat.shub.us'
    pro_meta ='http://apollo-pro.shub.us'
 
    if env == 'test' or env=='fat':
        url = fat_meta
    elif env == 'dev':
        url = dev_meta
    elif env == 'uat':
        url = uat_meta
    elif env == 'pro':
        url = pro_meta
    else:
        print_color(31, "==> Can't get the Apollo Meta")
        sys.exit(1)
        
    r = requests.get("{0}/configfiles/json/{1}/{2}/{3}".format(url,appid,cluster,namespace))
    if r.status_code == 200:
        with open('.env', 'w') as f:
            for k,v in r.json().items():
                f.write("{0}={1}\n".format(k,v))
    else:
        print_color(31, ">>> Can't connect to %s" % url)
        sys.exit(1)

