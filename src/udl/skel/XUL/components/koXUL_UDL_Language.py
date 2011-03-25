# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
# 
# The contents of this file are subject to the Mozilla Public License
# Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
# 
# Software distributed under the License is distributed on an "AS IS"
# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
# License for the specific language governing rights and limitations
# under the License.
# 
# The Original Code is Komodo code.
# 
# The Initial Developer of the Original Code is ActiveState Software Inc.
# Portions created by ActiveState Software Inc are Copyright (C) 2000-2007
# ActiveState Software Inc. All Rights Reserved.
# 
# Contributor(s):
#   ActiveState Software Inc
# 
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
# 
# ***** END LICENSE BLOCK *****

# Komodo XUL language service.
#
# Generated by 'luddite.py' on Fri Oct 20 08:49:16 2006.
#

import logging
from koXMLLanguageBase import koXMLLanguageBase, KoGenericXMLLinter


log = logging.getLogger("koXULLanguage")
#log.setLevel(logging.DEBUG)


def registerLanguage(registry):
    log.debug("Registering language XUL")
    registry.registerLanguage(KoXULLanguage())


class KoXULLanguage(koXMLLanguageBase):
    name = "XUL"
    lexresLangName = "XUL"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_clsid_ = "{E9B4C1F5-C9F9-4F85-A920-09A9A74B0950}"
    defaultExtension = '.xul'

    lang_from_udl_family = {'CSL': 'JavaScript', 'M': 'XML'}

    publicIdList = ["-//MOZILLA//DTD XUL V1.0//EN"]
    systemIdList = ["http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"]
    namespaces = ["http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"]

    searchURL = "http://www.google.com/search?q=site%3Ahttp%3A%2F%2Fdeveloper.mozilla.org%2Fen%2Fdocs%2FXUL+%W"

    sample = """<window title="Hello World!"
  xmlns="http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"
  width="250"
  height="200"> 

  <hbox flex="1" align="center">
    <image src="mozilla-big.gif" />
    <text style="font-weight: bold;" value="Hello World!" />
  </hbox>
</window>
"""

class KoXULCompileLinter(KoGenericXMLLinter):
    _reg_desc_ = "Komodo XUL Compile Linter"
    _reg_clsid_ = "{c097c54e-847b-42aa-81c0-3de0a71bcd08}"
    _reg_contractid_ = "@activestate.com/koLinter?language=XUL;1"
    _reg_categories_ = [
         ("category-komodo-linter", 'XUL'),
         ]
