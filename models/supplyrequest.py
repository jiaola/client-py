#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


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
class SupplyRequestParameter(backboneelement.BackboneElement):
    """ Ordered item details.

    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """
    resource_type: ClassVar[str] = "SupplyRequestParameter"
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
        js = super(SupplyRequestParameter, self).elementProperties()
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
class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    resource_type: ClassVar[str] = "SupplyRequest"
    authoredOn: Optional[fhirdate.FHIRDate] = None
    category: Optional[codeableconcept.CodeableConcept] = None
    deliverFrom: Optional[fhirreference.FHIRReference] = None
    deliverTo: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    itemCodeableConcept:codeableconcept.CodeableConcept = None
    itemReference:fhirreference.FHIRReference = None
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    parameter: Optional[List[SupplyRequestParameter]] = empty_list()
    priority: Optional[str] = None
    quantity:quantity.Quantity = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None
    supplier: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("deliverFrom", "deliverFrom", fhirreference.FHIRReference, False, None, False),
            ("deliverTo", "deliverTo", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", SupplyRequestParameter, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
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