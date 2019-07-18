#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing

from . import domainresource

@dataclass
class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    resource_type: ClassVar[str] = "DeviceUseStatement"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    derivedFrom: Optional[List[fhirreference.FHIRReference]] = empty_list()
    device:fhirreference.FHIRReference = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    recordedOn: Optional[fhirdate.FHIRDate] = None
    source: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject:fhirreference.FHIRReference = None
    timingDateTime: Optional[fhirdate.FHIRDate] = None
    timingPeriod: Optional[period.Period] = None
    timingTiming: Optional[timing.Timing] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']