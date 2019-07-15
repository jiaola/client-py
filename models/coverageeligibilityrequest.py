#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2019-07-15.
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
from . import money
from . import period
from . import quantity

from . import domainresource

@dataclass
class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.

    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequest"
    created:fhirdate.FHIRDate = None
    enterer: Optional[fhirreference.FHIRReference] = None
    facility: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    insurance: Optional[List[CoverageEligibilityRequestInsurance]] = empty_list()
    insurer:fhirreference.FHIRReference = None
    item: Optional[List[CoverageEligibilityRequestItem]] = empty_list()
    patient:fhirreference.FHIRReference = None
    priority: Optional[codeableconcept.CodeableConcept] = None
    provider: Optional[fhirreference.FHIRReference] = None
    purpose: List[ str] = empty_list()
    servicedDate: Optional[fhirdate.FHIRDate] = None
    servicedPeriod: Optional[period.Period] = None
    status: str = None
    supportingInfo: Optional[List[CoverageEligibilityRequestSupportingInfo]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestInsurance"
    businessArrangement: Optional[str] = None
    coverage:fhirreference.FHIRReference = None
    focal: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, False),
        ])
        return js

@dataclass
class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Item to be evaluated for eligibiity.

    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItem"
    category: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[List[fhirreference.FHIRReference]] = empty_list()
    diagnosis: Optional[List[CoverageEligibilityRequestItemDiagnosis]] = empty_list()
    facility: Optional[fhirreference.FHIRReference] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    productOrService: Optional[codeableconcept.CodeableConcept] = None
    provider: Optional[fhirreference.FHIRReference] = None
    quantity: Optional[quantity.Quantity] = None
    supportingInfoSequence: Optional[List[int]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ Applicable diagnosis.

    Patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItemDiagnosis"
    diagnosisCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    diagnosisReference: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
        ])
        return js

@dataclass
class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestSupportingInfo"
    appliesToAll: Optional[bool] = None
    information:fhirreference.FHIRReference = None
    sequence: int = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("information", "information", fhirreference.FHIRReference, False, None, True),
            ("sequence", "sequence", int, False, None, True),
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