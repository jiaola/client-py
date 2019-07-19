#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

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
class SupplyRequestParameter(BackboneElement):
    """ Ordered item details.

    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """
    resource_type: ClassVar[str] = "SupplyRequestParameter"
    code: Optional[CodeableConcept] = None
    valueBoolean: Optional[bool] = None
    valueCodeableConcept: Optional[CodeableConcept] = None
    valueQuantity: Optional[Quantity] = None
    valueRange: Optional[Range] = None

    def elementProperties(self):
        js = super(SupplyRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueRange", "valueRange", Range, False, "value", False),
        ])
        return js


@dataclass
class SupplyRequest(DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    resource_type: ClassVar[str] = "SupplyRequest"
    authoredOn: Optional[FHIRDate] = None
    category: Optional[CodeableConcept] = None
    deliverFrom: Optional[FHIRReference] = None
    deliverTo: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    parameter: Optional[List[SupplyRequestParameter]] = empty_list()
    priority: Optional[str] = None
    quantity: Quantity = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    requester: Optional[FHIRReference] = None
    status: Optional[str] = None
    supplier: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("deliverFrom", "deliverFrom", FHIRReference, False, None, False),
            ("deliverTo", "deliverTo", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("parameter", "parameter", SupplyRequestParameter, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantity", "quantity", Quantity, False, None, True),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("supplier", "supplier", FHIRReference, True, None, False),
        ])
        return js