#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Coverage) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity

from . import backboneelement

@dataclass
class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.

    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiaryException"
    period: Optional[period.Period] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.

    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    resource_type: ClassVar[str] = "CoverageCostToBeneficiary"
    exception: Optional[List[CoverageCostToBeneficiaryException]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    valueMoney:money.Money = None
    valueQuantity:quantity.Quantity = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
        ])
        return js

@dataclass
class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.

    A suite of underwriter specific classifiers.
    """
    resource_type: ClassVar[str] = "CoverageClass"
    name: Optional[str] = None
    type:codeableconcept.CodeableConcept = None
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    resource_type: ClassVar[str] = "Coverage"
    beneficiary:fhirreference.FHIRReference = None
    class_fhir: Optional[List[CoverageClass]] = empty_list()
    contract: Optional[List[fhirreference.FHIRReference]] = empty_list()
    costToBeneficiary: Optional[List[CoverageCostToBeneficiary]] = empty_list()
    dependent: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    network: Optional[str] = None
    order: Optional[int] = None
    payor: List[fhirreference.FHIRReference] = empty_list()
    period: Optional[period.Period] = None
    policyHolder: Optional[fhirreference.FHIRReference] = None
    relationship: Optional[codeableconcept.CodeableConcept] = None
    status: str = None
    subrogation: Optional[bool] = None
    subscriber: Optional[fhirreference.FHIRReference] = None
    subscriberId: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", str, False, None, False),
            ("order", "order", int, False, None, False),
            ("payor", "payor", fhirreference.FHIRReference, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subrogation", "subrogation", bool, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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