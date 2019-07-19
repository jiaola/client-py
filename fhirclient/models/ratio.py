#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Ratio) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .element import Element
from .quantity import Quantity


@dataclass
class Ratio(Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type: ClassVar[str] = "Ratio"
    denominator: Optional[Quantity] = None
    numerator: Optional[Quantity] = None

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("denominator", "denominator", Quantity, False, None, False),
            ("numerator", "numerator", Quantity, False, None, False),
        ])
        return js