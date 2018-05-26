#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `revisiondict` package."""

import sys

from revisiondict import RevisionDict

if sys.version_info[0] < 3:
    from test import util_mapping_py2 as util_mapping
else:
    from test import util_mapping_py3 as util_mapping


class RevisionDictMappingTest(util_mapping.TestMappingProtocol):
    # test compatability with MappingProtocol
    type2test = RevisionDict
