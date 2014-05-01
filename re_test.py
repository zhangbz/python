#!/usr/bin/env python
# coding=utf-8

import re
test = 'bill.gates@microsoft.com'
if re.match(r'^([\w\.]+)\@(\w+\.com)$', test):
    print 'ok'
print re.match(r'^([\w\.]+)\@(\w+\.com)$', test).groups()
