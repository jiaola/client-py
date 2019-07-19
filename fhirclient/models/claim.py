#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Claim) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
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
class ClaimSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ClaimSupportingInfo"
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    reason: Optional[CodeableConcept] = None
    sequence: int = None
    timingDate: Optional[FHIRDate] = None
    timingPeriod: Optional[Period] = None
    valueAttachment: Optional[Attachment] = None
    valueBoolean: Optional[bool] = None
    valueQuantity: Optional[Quantity] = None
    valueReference: Optional[FHIRReference] = None
    valueString: Optional[str] = None

    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("timingDate", "timingDate", FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueQuantity", "valueQuantity", Quantity, False, "value", False),
            ("valueReference", "valueReference", FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


@dataclass
class ClaimRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ClaimRelated"
    claim: Optional[FHIRReference] = None
    reference: Optional[Identifier] = None
    relationship: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", FHIRReference, False, None, False),
            ("reference", "reference", Identifier, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ClaimProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ClaimProcedure"
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = None
    procedureReference: FHIRReference = None
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()
    udi: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", CodeableConcept, True, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class ClaimPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ClaimPayee"
    party: Optional[FHIRReference] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ClaimItemDetailSubDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetailSubDetail"
    category: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    revenue: Optional[CodeableConcept] = None
    sequence: int = None
    udi: Optional[List[FHIRReference]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("udi", "udi", FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ClaimItemDetail(BackboneElement):
    """ Product or service provided.

    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimItemDetail"
    category: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    revenue: Optional[CodeableConcept] = None
    sequence: int = None
    subDetail: Optional[List[ClaimItemDetailSubDetail]] = empty_list()
    udi: Optional[List[FHIRReference]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ClaimItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimItem"
    bodySite: Optional[CodeableConcept] = None
    careTeamSequence: Optional[List[int]] = empty_list()
    category: Optional[CodeableConcept] = None
    detail: Optional[List[ClaimItemDetail]] = empty_list()
    diagnosisSequence: Optional[List[int]] = empty_list()
    encounter: Optional[List[FHIRReference]] = empty_list()
    factor: Optional[float] = None
    informationSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[Address] = None
    locationCodeableConcept: Optional[CodeableConcept] = None
    locationReference: Optional[FHIRReference] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    procedureSequence: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    revenue: Optional[CodeableConcept] = None
    sequence: int = None
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    subSite: Optional[List[CodeableConcept]] = empty_list()
    udi: Optional[List[FHIRReference]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("subSite", "subSite", CodeableConcept, True, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ClaimInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimInsurance"
    businessArrangement: Optional[str] = None
    claimResponse: Optional[FHIRReference] = None
    coverage: FHIRReference = None
    focal: bool = None
    identifier: Optional[Identifier] = None
    preAuthRef: Optional[List[str]] = empty_list()
    sequence: int = None

    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("identifier", "identifier", Identifier, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


@dataclass
class ClaimDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ClaimDiagnosis"
    diagnosisCodeableConcept: CodeableConcept = None
    diagnosisReference: FHIRReference = None
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", CodeableConcept, False, None, False),
            ("packageCode", "packageCode", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class ClaimCareTeam(BackboneElement):
    """ Members of the care team.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ClaimCareTeam"
    provider: FHIRReference = None
    qualification: Optional[CodeableConcept] = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    sequence: int = None

    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", FHIRReference, False, None, True),
            ("qualification", "qualification", CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


@dataclass
class ClaimAccident(BackboneElement):
    """ Details of the event.

    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ClaimAccident"
    date: FHIRDate = None
    locationAddress: Optional[Address] = None
    locationReference: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, True),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class Claim(DomainResource):
    """ Claim, Pre-determination or Pre-authorization.

    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    resource_type: ClassVar[str] = "Claim"
    accident: Optional[ClaimAccident] = None
    billablePeriod: Optional[Period] = None
    careTeam: Optional[List[ClaimCareTeam]] = empty_list()
    created: FHIRDate = None
    diagnosis: Optional[List[ClaimDiagnosis]] = empty_list()
    enterer: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    fundsReserve: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurance: List[ClaimInsurance] = empty_list()
    insurer: Optional[FHIRReference] = None
    item: Optional[List[ClaimItem]] = empty_list()
    originalPrescription: Optional[FHIRReference] = None
    patient: FHIRReference = None
    payee: Optional[ClaimPayee] = None
    prescription: Optional[FHIRReference] = None
    priority: CodeableConcept = None
    procedure: Optional[List[ClaimProcedure]] = empty_list()
    provider: FHIRReference = None
    referral: Optional[FHIRReference] = None
    related: Optional[List[ClaimRelated]] = empty_list()
    status: str = None
    subType: Optional[CodeableConcept] = None
    supportingInfo: Optional[List[ClaimSupportingInfo]] = empty_list()
    total: Optional[Money] = None
    type: CodeableConcept = None
    use: str = None

    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("billablePeriod", "billablePeriod", Period, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, True),
            ("insurer", "insurer", FHIRReference, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("originalPrescription", "originalPrescription", FHIRReference, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", FHIRReference, False, None, False),
            ("priority", "priority", CodeableConcept, False, None, True),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("provider", "provider", FHIRReference, False, None, True),
            ("referral", "referral", FHIRReference, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False),
            ("total", "total", Money, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js