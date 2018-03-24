#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `revisiondict` package."""

import pytest
from tests import util_mapping

from revisiondict import RevisionDict

class RevisionDictMappingTest(util_mapping.TestMappingProtocol):
  # test compatability with MappingProtocol
  type2test=RevisionDict
