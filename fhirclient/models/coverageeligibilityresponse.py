#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse) on 2019-07-18.
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


@dataclass
class CoverageEligibilityResponseInsuranceItemBenefit(BackboneElement):
    """ Benefit Summary.

    Benefits used to date.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItemBenefit"
    allowedMoney: Optional[Money] = None
    allowedString: Optional[str] = None
    allowedUnsignedInt: Optional[int] = None
    type: CodeableConcept = None
    usedMoney: Optional[Money] = None
    usedString: Optional[str] = None
    usedUnsignedInt: Optional[int] = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", Money, False, "used", False),
            ("usedString", "usedString", str, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseInsuranceItem(BackboneElement):
    """ Benefits and authorization details.

    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsuranceItem"
    authorizationRequired: Optional[bool] = None
    authorizationSupporting: Optional[List[CodeableConcept]] = empty_list()
    authorizationUrl: Optional[str] = None
    benefit: Optional[List[CoverageEligibilityResponseInsuranceItemBenefit]] = empty_list()
    category: Optional[CodeableConcept] = None
    description: Optional[str] = None
    excluded: Optional[bool] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    name: Optional[str] = None
    network: Optional[CodeableConcept] = None
    productOrService: Optional[CodeableConcept] = None
    provider: Optional[FHIRReference] = None
    term: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", CodeableConcept, True, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", CodeableConcept, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("term", "term", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseInsurance"
    benefitPeriod: Optional[Period] = None
    coverage: FHIRReference = None
    inforce: Optional[bool] = None
    item: Optional[List[CoverageEligibilityResponseInsuranceItem]] = empty_list()

    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("benefitPeriod", "benefitPeriod", Period, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("inforce", "inforce", bool, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
        ])
        return js


@dataclass
class CoverageEligibilityResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the request.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponseError"
    code: CodeableConcept = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class CoverageEligibilityResponse(DomainResource):
    """ CoverageEligibilityResponse resource.

    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    resource_type: ClassVar[str] = "CoverageEligibilityResponse"
    created: FHIRDate = None
    disposition: Optional[str] = None
    error: Optional[List[CoverageEligibilityResponseError]] = empty_list()
    form: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurance: Optional[List[CoverageEligibilityResponseInsurance]] = empty_list()
    insurer: FHIRReference = None
    outcome: str = None
    patient: FHIRReference = None
    preAuthRef: Optional[str] = None
    purpose: List[str] = empty_list()
    request: FHIRReference = None
    requestor: Optional[FHIRReference] = None
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    status: str = None

    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", FHIRDate, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
            ("form", "form", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("request", "request", FHIRReference, False, None, True),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
        ])
        return js