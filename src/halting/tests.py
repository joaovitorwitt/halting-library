##################################################
# Imports
##################################################
# pylint: disable=unused-import
from src.halting._tests.base import BaseHaltingTestCase
from src.halting._tests.utils import UtilsTestCase
from src.halting._tests.settings import SettingsTestCase


from src.halting.core.tests import *
from src.halting.math.tests import *
from src.halting.physics.tests import *

# from src.halting.math._tests import *
# from src.halting.physics._tests import *
# from src.halting._tests import *

"""
missing imports from other modules as well
"""

##################################################
# Explanation
##################################################

"""

This file will import all the test cases from the subdirectories,
following the pattern above.

"""
