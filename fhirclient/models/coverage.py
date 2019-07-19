#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Coverage) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class CoverageCostToBeneficiaryException(BackboneElement):
    """ Exceptions for patient payments.

    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiaryException"
    period: Optional[Period] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("period", "period", Period, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class CoverageCostToBeneficiary(BackboneElement):
    """ Patient payments for services/products.

    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiary"
    exception: Optional[List[CoverageCostToBeneficiaryException]] = empty_list()
    type: Optional[CodeableConcept] = None
    valueMoney: Money = None
    valueQuantity: Quantity = None

    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("valueMoney", "valueMoney", Money, False, "value", True),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", True),
        ])
        return js


@dataclass
class CoverageClass(BackboneElement):
    """ Additional coverage classifications.

    A suite of underwriter specific classifiers.
    """
    resource_type: ClassVar[str] = "CoverageClass"
    name: Optional[str] = None
    type: CodeableConcept = None
    value: str = None

    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class Coverage(DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    resource_type: ClassVar[str] = "Coverage"
    beneficiary: FHIRReference = None
    class_fhir: Optional[List[CoverageClass]] = empty_list()
    contract: Optional[List[FHIRReference]] = empty_list()
    costToBeneficiary: Optional[List[CoverageCostToBeneficiary]] = empty_list()
    dependent: Optional[str] = None
    identifier: Optional[List[Identifier]] = empty_list()
    network: Optional[str] = None
    order: Optional[int] = None
    payor: List[FHIRReference] = empty_list()
    period: Optional[Period] = None
    policyHolder: Optional[FHIRReference] = None
    relationship: Optional[CodeableConcept] = None
    status: str = None
    subrogation: Optional[bool] = None
    subscriber: Optional[FHIRReference] = None
    subscriberId: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", FHIRReference, False, None, True),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("contract", "contract", FHIRReference, True, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("network", "network", str, False, None, False),
            ("order", "order", int, False, None, False),
            ("payor", "payor", FHIRReference, True, None, True),
            ("period", "period", Period, False, None, False),
            ("policyHolder", "policyHolder", FHIRReference, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subrogation", "subrogation", bool, False, None, False),
            ("subscriber", "subscriber", FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js