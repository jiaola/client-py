#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .quantity import Quantity
from .range import Range
from .timing import Timing


@dataclass
class DeviceRequestParameter(BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    resource_type: ClassVar[str] = "DeviceRequestParameter"
    code: Optional[CodeableConcept] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
        ])
        return js


@dataclass
class DeviceRequest(DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"
    authoredOn: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    codeCodeableConcept: CodeableConcept = None
    codeReference: FHIRReference = None
    encounter: Optional[FHIRReference] = None
    groupIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[FHIRReference]] = empty_list()
    intent: str = None
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    parameter: Optional[List[DeviceRequestParameter]] = empty_list()
    performer: Optional[FHIRReference] = None
    performerType: Optional[CodeableConcept] = None
    priorRequest: Optional[List[FHIRReference]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    relevantHistory: Optional[List[FHIRReference]] = empty_list()
    requester: Optional[FHIRReference] = None
    status: Optional[str] = None
    subject: FHIRReference = None
    supportingInfo: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", FHIRReference, False, "code", True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("priorRequest", "priorRequest", FHIRReference, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
        ])
        return js