"""
Misc tests.

File: test_misc.py

Copyright 2021 LEMS contributors
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>
"""


import unittest
from lems.model.model import Model


class TestExposure(unittest.TestCase):

    """Test getting exposures from LEMS models"""

    def test_exposure_getters(self):
        model = Model(include_includes=True, fail_on_missing_includes=True)
        file_name = 'examples/example1.xml'
        model.import_from_file(file_name)
        exp_list = model.list_exposures()
        for c, es in exp_list.items():
            # iaf1 does not define v as an exposure
            if c.id == "ctb":
                self.assertTrue('v' not in es)
            # iaf2 extends iaf1 and adds the v exposure
            if c.id == "ctd":
                self.assertTrue('v' in es)
                self.assertTrue('tsince' not in es)
            # iaf3 extends iaf2 so inherits the v exposure
            if c.id == "celltype_c":
                self.assertTrue('v' in es)
                self.assertTrue('tsince' not in es)
            if c.id == "gen1":
                self.assertTrue('v' not in es)
                self.assertTrue('tsince' in es)


if __name__ == '__main__':
    unittest.main()
