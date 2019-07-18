#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Address) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import period

from . import element

@dataclass
class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    resource_type: ClassVar[str] = "Address"
    city: Optional[str] = None
    country: Optional[str] = None
    district: Optional[str] = None
    line: Optional[List[str]] = empty_list()
    period: Optional[period.Period] = None
    postalCode: Optional[str] = None
    state: Optional[str] = None
    text: Optional[str] = None
    type: Optional[str] = None
    use: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, False, None, False),
            ("country", "country", str, False, None, False),
            ("district", "district", str, False, None, False),
            ("line", "line", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']