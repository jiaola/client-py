#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2019-07-18.
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
from .money import Money
from .period import Period
from .quantity import Quantity
from .timing import Timing


@dataclass
class ChargeItemPerformer(BackboneElement):
    """ Who performed charged service.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "ChargeItemPerformer"
    actor: FHIRReference = None
    function: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("function", "function", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ChargeItem(DomainResource):
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
    account: Optional[List[FHIRReference]] = empty_list()
    bodysite: Optional[List[CodeableConcept]] = empty_list()
    code: CodeableConcept = None
    context: Optional[FHIRReference] = None
    costCenter: Optional[FHIRReference] = None
    definitionCanonical: Optional[List[str]] = empty_list()
    definitionUri: Optional[List[str]] = empty_list()
    enteredDate: Optional[FHIRDate] = None
    enterer: Optional[FHIRReference] = None
    factorOverride: Optional[float] = None
    identifier: Optional[List[Identifier]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    occurrenceTiming: Optional[Timing] = None
    overrideReason: Optional[str] = None
    partOf: Optional[List[FHIRReference]] = empty_list()
    performer: Optional[List[ChargeItemPerformer]] = empty_list()
    performingOrganization: Optional[FHIRReference] = None
    priceOverride: Optional[Money] = None
    productCodeableConcept: Optional[CodeableConcept] = None
    productReference: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    reason: Optional[List[CodeableConcept]] = empty_list()
    requestingOrganization: Optional[FHIRReference] = None
    service: Optional[List[FHIRReference]] = empty_list()
    status: str = None
    subject: FHIRReference = None
    supportingInformation: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("account", "account", FHIRReference, True, None, False),
            ("bodysite", "bodysite", CodeableConcept, True, None, False),
            ("code", "code", CodeableConcept, False, None, True),
            ("context", "context", FHIRReference, False, None, False),
            ("costCenter", "costCenter", FHIRReference, False, None, False),
            ("definitionCanonical", "definitionCanonical", str, True, None, False),
            ("definitionUri", "definitionUri", str, True, None, False),
            ("enteredDate", "enteredDate", FHIRDate, False, None, False),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", Timing, False, "occurrence", False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("partOf", "partOf", FHIRReference, True, None, False),
            ("performer", "performer", ChargeItemPerformer, True, None, False),
            ("performingOrganization", "performingOrganization", FHIRReference, False, None, False),
            ("priceOverride", "priceOverride", Money, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", CodeableConcept, False, "product", False),
            ("productReference", "productReference", FHIRReference, False, "product", False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("reason", "reason", CodeableConcept, True, None, False),
            ("requestingOrganization", "requestingOrganization", FHIRReference, False, None, False),
            ("service", "service", FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", FHIRReference, True, None, False),
        ])
        return js