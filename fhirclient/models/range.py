#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Range) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .quantity import Quantity


@dataclass
class Range(Element):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """
    resource_type: ClassVar[str] = "Range"
    high: Optional[Quantity] = None
    low: Optional[Quantity] = None

    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("high", "high", Quantity, False, None, False),
            ("low", "low", Quantity, False, None, False),
        ])
        return js