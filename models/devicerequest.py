#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import timing

from . import backboneelement

@dataclass
class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    resource_type: ClassVar[str] = "DeviceRequestParameter"
    code: Optional[codeableconcept.CodeableConcept] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueRange: Optional[range.Range] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
        ])
        return js

from . import domainresource

@dataclass
class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    resource_type: ClassVar[str] = "DeviceRequest"
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    codeCodeableConcept:codeableconcept.CodeableConcept = None
    codeReference:fhirreference.FHIRReference = None
    encounter: Optional[fhirreference.FHIRReference] = None
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    insurance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    intent: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    parameter: Optional[List[DeviceRequestParameter]] = empty_list()
    performer: Optional[fhirreference.FHIRReference] = None
    performerType: Optional[codeableconcept.CodeableConcept] = None
    priorRequest: Optional[List[fhirreference.FHIRReference]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    relevantHistory: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None
    subject:fhirreference.FHIRReference = None
    supportingInfo: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']