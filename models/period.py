#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Period) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import element
from . import fhirdate

from . import element

@dataclass
class Period(element.Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """
    resource_type: ClassVar[str] = "Period"
    end: Optional[fhirdate.FHIRDate] = None
    start: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']