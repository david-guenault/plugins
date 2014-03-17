#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
Copyright (C) 2009-2012:
    David GUENAULT, david.guenault@gmail.com

checkmyws.py is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

checkmyws.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with checkmyws.py.  If not, see <http://www.gnu.org/licenses/>.

checkmyws.py requires Python 2.6, but does not support Python 3.x yet.
"""

import sys
import requests
import json
import getopt
import argparse

""" Nagios standard return codes """
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

""" rest service methods """

""" base api url """
url = "https://console.checkmy.ws/api"

""" authentication on rest api """
""" need a json payload with login and password fields """
""" password field must be SHA1 encoded """
login = "/api/auth/signin"

""" Logout from rest api """
logout = "/api/auth/logout"

""" Get checks data """
checks = "/api/checks"

""" checkmyws base url """
website = "http://www.shinken.io"


def parseStatusCode(req):
    """ get status code """
    if req.status_code == 200:
        """ (200) everything seem fine """
        return
    elif req.status_code == 401:
        """ (401) Authentication failure """
        print "[UNKNOWN] Authentication failure to webservice"
        sys.exit(UNKNOWN)
    elif req.status_code == 500:
        """ (500) Internal Server Error """
        print "[UNKNOWN] Remote application server unavailable"
        sys.exit(UNKNOWN)
    elif req.status_code == 404:
        """ (404) Page not found """
        print "[UNKNOWN] Remote webservice not found"
        sys.exit(UNKNOWN)
    else:
        """ Unknown error """
        print "[UNKNOWN] Unknown error ..."
        sys.exit(UNKNOWN)


def authenticate(username, password):
    """ Prepare json payload and headers """
    payload = {"login": username, "passwd": password}
    headers = {"content-type": "application/json"}

    """ First encode payload in json format """
    try:
        data = json.dumps(payload)
    except:
        print "[UNKNOWN] Unable to encode json payload"
        sys.exit(UNKNOWN)

    """ auth """
    req = requests.post(url, data=data, headers=headers)

    """ parse status code """
    parseStatusCode(req)

def usage():
    print "checkmyws.py -u username -p password -s url"
    return

if __name__ == "__main__":
    username = ""
    password = ""
    url = ""

    parser = argpars.ArgumentParser(description='')
    parser.add_argument('username',metavar='N', type=string

    if not username or not password or not url:
        print "[UNKNOWN] username password and url are mandatory"
        sys.exit(UNKNOWN)

    authenticate(username, password)
