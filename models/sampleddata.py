#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SampledData) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import quantity

from . import element

@dataclass
class SampledData(element.Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    resource_type: ClassVar[str] = "SampledData"
    data: Optional[str] = None
    dimensions: int = None
    factor: Optional[float] = None
    lowerLimit: Optional[float] = None
    origin:quantity.Quantity = None
    period: float = None
    upperLimit: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("factor", "factor", float, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("upperLimit", "upperLimit", float, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']