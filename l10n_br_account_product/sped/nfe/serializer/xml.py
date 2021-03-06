# -*- coding: utf-8 -*-
###############################################################################
#                                                                             #
# Copyright (C) 200(  Renato Lima - Akretion                                  #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from ..document import NFe200
from ..document import NFe310


def nfe_export(cr, uid, ids, nfe_environment='1',
               nfe_version='2.00', context=None):

    if nfe_version == '3.10':
        NFe = NFe310()
    else:
        NFe = NFe200()

    nfes = NFe.get_xml(cr, uid, ids, nfe_environment, context)

    return nfes
