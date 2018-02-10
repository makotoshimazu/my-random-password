#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# generator.py
# 
# Author:   Makoto Shimazu <makoto.shimaz@gmail.com>
# URL:      https://amiq11.tumblr.com               
# License:  2-Clause BSD License                    
# Created:  2018-02-10                              
#
#
# Copyright (c) 2018, Makoto Shimazu
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import random

class Generator():
    def __init__(self, option):
        random.seed()
        self._length = option['length'] if 'length' in option else 12
        self._numbers = option['numbers'] if 'numbers' in option else False
        self._lower_alphabet = option['lower_alphabet'] if 'lower_alphabet' in option else False
        self._upper_alphabet = option['upper_alphabet'] if 'upper_alphabet' in option else False
        self._symbols = option['symbols'] if 'symbols' in option else False

    def generate(self):
        candidate = ""
        if (self._numbers):
            candidate += "0123456789"
        if (self._lower_alphabet):
            candidate += "abcdefghijklmnopqrstuvwxyz"
        if (self._upper_alphabet):
            candidate += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if (self._symbols):
            candidate += "$@!?;:,.+=_"
        out = ""
        for i in range(self._length):
            pos = random.randrange(0, len(candidate))
            out += candidate[pos]
        return out

if __name__ == '__main__':
    generator = Generator({
        'length': 16,
        'numbers': True,
        'lower_alphabet': True,
        'upper_alphabet': True})
    print(generator.generate())
