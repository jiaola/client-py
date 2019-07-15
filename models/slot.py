#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Slot) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    resource_type: ClassVar[str] = "Slot"
    appointmentType: Optional[codeableconcept.CodeableConcept] = None
    comment: Optional[str] = None
    end:fhirdate.FHIRDate = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    overbooked: Optional[bool] = None
    schedule:fhirreference.FHIRReference = None
    serviceCategory: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    serviceType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    specialty: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    start:fhirdate.FHIRDate = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("overbooked", "overbooked", bool, False, None, False),
            ("schedule", "schedule", fhirreference.FHIRReference, False, None, True),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, True),
            ("status", "status", str, False, None, True),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']