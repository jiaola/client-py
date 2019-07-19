#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2019-07-18.
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
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class CoverageEligibilityRequestSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestSupportingInfo"
    appliesToAll: Optional[bool] = None
    information: FHIRReference = None
    sequence: int = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("information", "information", FHIRReference, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


@dataclass
class CoverageEligibilityRequestItemDiagnosis(BackboneElement):
    """ Applicable diagnosis.

    Patient diagnosis for which care is sought.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItemDiagnosis"
    diagnosisCodeableConcept: Optional[CodeableConcept] = None
    diagnosisReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", FHIRReference, False, "diagnosis", False),
        ])
        return js


@dataclass
class CoverageEligibilityRequestItem(BackboneElement):
    """ Item to be evaluated for eligibiity.

    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestItem"
    category: Optional[CodeableConcept] = None
    detail: Optional[List[FHIRReference]] = empty_list()
    diagnosis: Optional[List[CoverageEligibilityRequestItemDiagnosis]] = empty_list()
    facility: Optional[FHIRReference] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    productOrService: Optional[CodeableConcept] = None
    provider: Optional[FHIRReference] = None
    quantity: Optional[Quantity] = None
    supportingInfoSequence: Optional[List[int]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("detail", "detail", FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityRequestInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequestInsurance"
    businessArrangement: Optional[str] = None
    coverage: FHIRReference = None
    focal: Optional[bool] = None

    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityRequest(DomainResource):
    """ CoverageEligibilityRequest resource.

    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityRequest"
    created: FHIRDate = None
    enterer: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurance: Optional[List[CoverageEligibilityRequestInsurance]] = empty_list()
    insurer: FHIRReference = None
    item: Optional[List[CoverageEligibilityRequestItem]] = empty_list()
    patient: FHIRReference = None
    priority: Optional[CodeableConcept] = None
    provider: Optional[FHIRReference] = None
    purpose: List[str] = empty_list()
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    status: str = None
    supportingInfo: Optional[List[CoverageEligibilityRequestSupportingInfo]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", FHIRDate, False, None, True),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
        ])
        return js