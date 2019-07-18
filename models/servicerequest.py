#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2019-07-18.
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
from . import quantity
from . import range
from . import ratio
from . import timing

from . import domainresource

@dataclass
class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.

    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    resource_type: ClassVar[str] = "ServiceRequest"
    asNeededBoolean: Optional[bool] = None
    asNeededCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodySite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code: Optional[codeableconcept.CodeableConcept] = None
    doNotPerform: Optional[bool] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    locationCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    locationReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    orderDetail: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    patientInstruction: Optional[str] = None
    performer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performerType: Optional[codeableconcept.CodeableConcept] = None
    priority: Optional[str] = None
    quantityQuantity: Optional[quantity.Quantity] = None
    quantityRange: Optional[range.Range] = None
    quantityRatio: Optional[ratio.Ratio] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    replaces: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    requisition: Optional[identifier.Identifier] = None
    specimen: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject:fhirreference.FHIRReference = None
    supportingInfo: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']