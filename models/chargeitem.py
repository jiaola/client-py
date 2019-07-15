#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2019-07-15.
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
from . import money
from . import period
from . import quantity
from . import timing

from . import domainresource

@dataclass
class ChargeItem(domainresource.DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.

    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """
    resource_type: ClassVar[str] = "ChargeItem"
    account: Optional[List[fhirreference.FHIRReference]] = empty_list()
    bodysite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    code:codeableconcept.CodeableConcept = None
    context: Optional[fhirreference.FHIRReference] = None
    costCenter: Optional[fhirreference.FHIRReference] = None
    definitionCanonical: Optional[List[str]] = empty_list()
    definitionUri: Optional[List[str]] = empty_list()
    enteredDate: Optional[fhirdate.FHIRDate] = None
    enterer: Optional[fhirreference.FHIRReference] = None
    factorOverride: Optional[float] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    occurrenceTiming: Optional[timing.Timing] = None
    overrideReason: Optional[str] = None
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    performer: Optional[List[ChargeItemPerformer]] = empty_list()
    performingOrganization: Optional[fhirreference.FHIRReference] = None
    priceOverride: Optional[money.Money] = None
    productCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    productReference: Optional[fhirreference.FHIRReference] = None
    quantity: Optional[quantity.Quantity] = None
    reason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    requestingOrganization: Optional[fhirreference.FHIRReference] = None
    service: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: str = None
    subject:fhirreference.FHIRReference = None
    supportingInformation: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("bodysite", "bodysite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("costCenter", "costCenter", fhirreference.FHIRReference, False, None, False),
            ("definitionCanonical", "definitionCanonical", str, True, None, False),
            ("definitionUri", "definitionUri", str, True, None, False),
            ("enteredDate", "enteredDate", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", ChargeItemPerformer, True, None, False),
            ("performingOrganization", "performingOrganization", fhirreference.FHIRReference, False, None, False),
            ("priceOverride", "priceOverride", money.Money, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("requestingOrganization", "requestingOrganization", fhirreference.FHIRReference, False, None, False),
            ("service", "service", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ChargeItemPerformer(backboneelement.BackboneElement):
    """ Who performed charged service.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "ChargeItemPerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
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