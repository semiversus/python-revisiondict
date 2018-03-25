#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `revisiondict` package."""

import pytest
import sys

if sys.version_info[0]<3:
  from tests import util_mapping_py2 as util_mapping
else:
  from tests import util_mapping_py3 as util_mapping

from revisiondict import RevisionDict

class RevisionDictMappingTest(util_mapping.TestMappingProtocol):
  # test compatability with MappingProtocol
  type2test=RevisionDict