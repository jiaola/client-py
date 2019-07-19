#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2019-07-18.
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
from .timing import Timing


@dataclass
class SupplyDeliverySuppliedItem(BackboneElement):
    """ The item that is delivered or supplied.

    The item that is being delivered or has been supplied.
    """
    resource_type: ClassVar[str] = "SupplyDeliverySuppliedItem"
    itemCodeableConcept: Optional[CodeableConcept] = None
    itemReference: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None

    def elementProperties(self):
        js = super(SupplyDeliverySuppliedItem, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", False),
            ("itemReference", "itemReference", FHIRReference, False, "item", False),
            ("quantity", "quantity", Quantity, False, None, False),
        ])
        return js


@dataclass
class SupplyDelivery(DomainResource):
    """ Delivery of bulk Supplies.

    Record of delivery of what is supplied.
    """
    resource_type: ClassVar[str] = "SupplyDelivery"
    basedOn: Optional[List[FHIRReference]] = empty_list()
    destination: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    patient: Optional[FHIRReference] = None
    receiver: Optional[List[FHIRReference]] = empty_list()
    status: Optional[str] = None
    suppliedItem: Optional[SupplyDeliverySuppliedItem] = None
    supplier: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("destination", "destination", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("patient", "patient", FHIRReference, False, None, False),
            ("receiver", "receiver", FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("suppliedItem", "suppliedItem", SupplyDeliverySuppliedItem, False, None, False),
            ("supplier", "supplier", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js