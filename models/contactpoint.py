#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import period

from . import element

@dataclass
class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    resource_type: ClassVar[str] = "ContactPoint"
    period: Optional[period.Period] = None
    rank: Optional[int] = None
    system: Optional[str] = None
    use: Optional[str] = None
    value: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("system", "system", str, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']