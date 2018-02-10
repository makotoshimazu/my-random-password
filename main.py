#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
#
# main.py
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


from flask import Flask, render_template, request
from generator import Generator

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_index(None)

@app.route('/', methods=['POST'])
def gen():
    options = {
        'numbers': True,
        'lower_alphabet': True,
        'upper_alphabet': True
    }
    if 'length' in request.form:
        options['length'] = int(request.form['length'])
    return render_index(options)

def render_index(options):
    if (options is None):
        return render_template('index.html')
    generator = Generator(options)
    out = generator.generate()
    return render_template(
        'index.html', passwords=[out])
