# -*- coding: utf-8 -*-
# Copyright: (c) 2022, joaopa
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
import re

# noinspection PyUnresolvedReferences
from codequick import Resolver, Script
import urlquick

from kodi_six import xbmcgui

from resources.lib import resolver_proxy, web_utils

# TODO
# Add Replay

URL_LIVE = "https://11554-1.b.cdn13.com/LiveHTTPOrigin/live/playlist.m3u8"


@Resolver.register
def get_live_url(plugin, item_id, **kwargs):

    headers = {
        'User-Agent': web_utils.get_random_ua(),
        'Referer': 'https://componentes.enlace.org'
    }
    rate = {
        0: "https://11554-1.b.cdn13.com/LiveHTTPOrigin/live_160p/playlist.m3u8",
        1: "https://11554-1.b.cdn13.com/LiveHTTPOrigin/live_360p/playlist.m3u8",
        2: "https://11554-1.b.cdn13.com/LiveHTTPOrigin/live/playlist.m3u8"
    }
    choose_rate = xbmcgui.Dialog().select(Script.localize(30174), ["160p", "360p", "480p"])
    video_url = rate[choose_rate]

    return resolver_proxy.get_stream_with_quality(plugin, video_url, headers=headers, manifest_type="hls", bypass=True)
