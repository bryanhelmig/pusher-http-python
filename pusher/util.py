# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import,
                        division)

import json
import re
import six
import sys

channel_name_re = re.compile('^[-a-zA-Z0-9_=@,.;]+$')
app_id_re       = re.compile('^[0-9]+$')
pusher_url_re   = re.compile('(http|https)://(.*):(.*)@(.*)/apps/([0-9]+)')

if sys.version_info < (3,):
    text = 'a unicode string'
else:
    text = 'a string'

def ensure_text(obj, name):
    if isinstance(obj, six.text_type):
        return obj
    if isinstance(obj, six.string_types):
       return six.text_type(obj)
    raise TypeError("%s should be %s" % (name, text))

def validate_channel(channel):
    channel = ensure_text(channel, "channel")

    if len(channel) > 200:
        raise ValueError("Channel too long: %s" % channel)

    if not channel_name_re.match(channel):
        raise ValueError("Invalid Channel: %s" % channel)

    return channel