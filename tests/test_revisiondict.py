#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `revisiondict` package."""

from revisiondict import RevisionDict, UniqueRevisionDict

from tests import util_mapping_py3 as util_mapping


class RevisionDictMappingTest(util_mapping.TestMappingProtocol):
    # test compatability with MappingProtocol
    type2test = RevisionDict


class UniqueRevisionDictMappingTest(util_mapping.TestMappingProtocol):
    # test compatability with MappingProtocol
    type2test = UniqueRevisionDict
