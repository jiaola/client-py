#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Range) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import quantity


from . import element

@dataclass
class Range(element.Element):
    """ Set of values bounded by low and high.

    A set of ordered Quantities defined by a low and high limit.
    """
    resource_type: ClassVar[str] = "Range"
    high: Optional[quantity.Quantity] = None
    low: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.high = None
#        """ High limit.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.low = None
#        """ Low limit.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#

#        super(Range, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("high", "high", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("low", "low", quantity.Quantity, {  # #}False, None, {  # #}False),
        ])
        return js