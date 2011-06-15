#!/usr/bin/env python
import fapws._evwsgi as evwsgi
from fapws import base
import app

evwsgi.start('0.0.0.0', '8080')
evwsgi.set_base_module(base)
evwsgi.wsgi_cb(('/', app.init()))
evwsgi.set_debug(0)
evwsgi.run()
