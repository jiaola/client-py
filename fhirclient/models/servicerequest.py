#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2019-07-18.
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
from .quantity import Quantity
from .range import Range
from .ratio import Ratio
from .timing import Timing


@dataclass
class ServiceRequest(DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    resource_type: ClassVar[str] = "ServiceRequest"
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[CodeableConcept] = None
    authoredOn: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    bodySite: Optional[List[CodeableConcept]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    code: Optional[CodeableConcept] = None
    doNotPerform: Optional[bool] = None
    encounter: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[FHIRReference]] = empty_list()
    intent: str = None
    locationCode: Optional[List[CodeableConcept]] = empty_list()
    locationReference: Optional[List[FHIRReference]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    orderDetail: Optional[List[CodeableConcept]] = empty_list()
    patientInstruction: Optional[str] = None
    performer: Optional[List[FHIRReference]] = empty_list()
    performerType: Optional[CodeableConcept] = None
    priority: Optional[str] = None
    quantityQuantity: Optional[Quantity] = None
    quantityRange: Optional[Range] = None
    quantityRatio: Optional[Ratio] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    relevantHistory: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    requester: Optional[FHIRReference] = None
    requisition: Optional[Identifier] = None
    specimen: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: FHIRReference = None
    supportingInfo: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("locationCode", "locationCode", CodeableConcept, True, None, False),
            ("locationReference", "locationReference", FHIRReference, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("orderDetail", "orderDetail", CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("performer", "performer", FHIRReference, True, None, False),
            ("performerType", "performerType", CodeableConcept, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantityQuantity", "quantityQuantity", Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", Range, False, "quantity", False),
            ("quantityRatio", "quantityRatio", Ratio, False, "quantity", False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("requisition", "requisition", Identifier, False, None, False),
            ("specimen", "specimen", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", FHIRReference, True, None, False),
        ])
        return js