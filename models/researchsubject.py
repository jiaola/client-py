#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import domainresource
from . import fhirreference
from . import identifier
from . import period

from . import domainresource

@dataclass
class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.

    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    resource_type: ClassVar[str] = "ResearchSubject"
    actualArm: Optional[str] = None
    assignedArm: Optional[str] = None
    consent: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    individual:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    status: str = None
    study:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, False, None, False),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("consent", "consent", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("individual", "individual", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("study", "study", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']