#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2019-07-15.
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
from . import timing

from . import domainresource

@dataclass
class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of bulk Supplies.

    Record of delivery of what is supplied.
    """
    resource_type: ClassVar[str] = "SupplyDelivery"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    destination: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    patient: Optional[fhirreference.FHIRReference] = None
    receiver: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[str] = None
    suppliedItem: Optional[SupplyDeliverySuppliedItem] = None
    supplier: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("suppliedItem", "suppliedItem", SupplyDeliverySuppliedItem, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SupplyDeliverySuppliedItem(backboneelement.BackboneElement):
    """ The item that is delivered or supplied.

    The item that is being delivered or has been supplied.
    """
    resource_type: ClassVar[str] = "SupplyDeliverySuppliedItem"
    itemCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    itemReference: Optional[fhirreference.FHIRReference] = None
    quantity: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SupplyDeliverySuppliedItem, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']