#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .timing import Timing


@dataclass
class DeviceUseStatement(DomainResource):
    """ Record of use of a device.

    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    resource_type: ClassVar[str] = "DeviceUseStatement"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    derivedFrom: Optional[List[FHIRReference]] = empty_list()
    device: FHIRReference = None
    identifier: Optional[List[Identifier]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    recordedOn: Optional[FHIRDate] = None
    source: Optional[FHIRReference] = None
    status: str = None
    subject: FHIRReference = None
    timingDateTime: Optional[FHIRDate] = None
    timingPeriod: Optional[Period] = None
    timingTiming: Optional[Timing] = None

    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", FHIRReference, True, None, False),
            ("device", "device", FHIRReference, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("recordedOn", "recordedOn", FHIRDate, False, None, False),
            ("source", "source", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("timingTiming", "timingTiming", Timing, False, "timing", False),
        ])
        return js