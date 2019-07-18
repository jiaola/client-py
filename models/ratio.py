#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Ratio) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import quantity

from . import element

@dataclass
class Ratio(element.Element):
    """ A ratio of two Quantity values - a numerator and a denominator.

    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """
    resource_type: ClassVar[str] = "Ratio"
    denominator: Optional[quantity.Quantity] = None
    numerator: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("denominator", "denominator", quantity.Quantity, False, None, False),
            ("numerator", "numerator", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']