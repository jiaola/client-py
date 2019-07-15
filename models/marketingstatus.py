#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MarketingStatus) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import period

from . import backboneelement

@dataclass
class MarketingStatus(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    resource_type: ClassVar[str] = "MarketingStatus"
    country:codeableconcept.CodeableConcept = None
    dateRange:period.Period = None
    jurisdiction: Optional[codeableconcept.CodeableConcept] = None
    restoreDate: Optional[fhirdate.FHIRDate] = None
    status:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MarketingStatus, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("dateRange", "dateRange", period.Period, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("restoreDate", "restoreDate", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']