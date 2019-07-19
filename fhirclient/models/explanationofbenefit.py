#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .address import Address
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .quantity import Quantity


@dataclass
class ExplanationOfBenefitTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitTotal"
    amount: Money = None
    category: CodeableConcept = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, True),
            ("category", "category", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ExplanationOfBenefitSupportingInfo(BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitSupportingInfo"
    category: CodeableConcept = None
    code: Optional[CodeableConcept] = None
    reason: Optional[Coding] = None
    sequence: int = None
    timingDate: Optional[FHIRDate] = None
    timingPeriod: Optional[Period] = None
    valueAttachment: Optional[Attachment] = None
    valueBoolean: Optional[bool] = None
    valueQuantity: Optional[Quantity] = None
    valueReference: Optional[FHIRReference] = None
    valueString: Optional[str] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("reason", "reason", Coding, False, None, False),
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
class ExplanationOfBenefitRelated(BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitRelated"
    claim: Optional[FHIRReference] = None
    reference: Optional[Identifier] = None
    relationship: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", FHIRReference, False, None, False),
            ("reference", "reference", Identifier, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcessNote"
    language: Optional[CodeableConcept] = None
    number: Optional[int] = None
    text: Optional[str] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitProcedure(BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcedure"
    date: Optional[FHIRDate] = None
    procedureCodeableConcept: CodeableConcept = None
    procedureReference: FHIRReference = None
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()
    udi: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
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
class ExplanationOfBenefitPayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayment"
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    amount: Optional[Money] = None
    date: Optional[FHIRDate] = None
    identifier: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", CodeableConcept, False, None, False),
            ("amount", "amount", Money, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitPayee(BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayee"
    party: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItemDetailSubDetail(BackboneElement):
    """ Additional items.

    Third-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetailSubDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    category: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    revenue: Optional[CodeableConcept] = None
    sequence: int = None
    udi: Optional[List[FHIRReference]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
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
class ExplanationOfBenefitItemDetail(BackboneElement):
    """ Additional items.

    Second-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    category: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    quantity: Optional[Quantity] = None
    revenue: Optional[CodeableConcept] = None
    sequence: int = None
    subDetail: Optional[List[ExplanationOfBenefitItemDetailSubDetail]] = empty_list()
    udi: Optional[List[FHIRReference]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("revenue", "revenue", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("udi", "udi", FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemAdjudication"
    amount: Optional[Money] = None
    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, False),
            ("category", "category", CodeableConcept, False, None, True),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitItem(BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItem"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    careTeamSequence: Optional[List[int]] = empty_list()
    category: Optional[CodeableConcept] = None
    detail: Optional[List[ExplanationOfBenefitItemDetail]] = empty_list()
    diagnosisSequence: Optional[List[int]] = empty_list()
    encounter: Optional[List[FHIRReference]] = empty_list()
    factor: Optional[float] = None
    informationSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[Address] = None
    locationCodeableConcept: Optional[CodeableConcept] = None
    locationReference: Optional[FHIRReference] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
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
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
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
class ExplanationOfBenefitInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInsurance"
    coverage: FHIRReference = None
    focal: bool = None
    preAuthRef: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitDiagnosis(BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitDiagnosis"
    diagnosisCodeableConcept: CodeableConcept = None
    diagnosisReference: FHIRReference = None
    onAdmission: Optional[CodeableConcept] = None
    packageCode: Optional[CodeableConcept] = None
    sequence: int = None
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
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
class ExplanationOfBenefitCareTeam(BackboneElement):
    """ Care Team members.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitCareTeam"
    provider: FHIRReference = None
    qualification: Optional[CodeableConcept] = None
    responsible: Optional[bool] = None
    role: Optional[CodeableConcept] = None
    sequence: int = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", FHIRReference, False, None, True),
            ("qualification", "qualification", CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


@dataclass
class ExplanationOfBenefitBenefitBalanceFinancial(BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalanceFinancial"
    allowedMoney: Optional[Money] = None
    allowedString: Optional[str] = None
    allowedUnsignedInt: Optional[int] = None
    type: CodeableConcept = None
    usedMoney: Optional[Money] = None
    usedUnsignedInt: Optional[int] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", Money, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
        ])
        return js


@dataclass
class ExplanationOfBenefitBenefitBalance(BackboneElement):
    """ Balance by Benefit Category.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalance"
    category: CodeableConcept = None
    description: Optional[str] = None
    excluded: Optional[bool] = None
    financial: Optional[List[ExplanationOfBenefitBenefitBalanceFinancial]] = empty_list()
    name: Optional[str] = None
    network: Optional[CodeableConcept] = None
    term: Optional[CodeableConcept] = None
    unit: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", CodeableConcept, False, None, False),
            ("term", "term", CodeableConcept, False, None, False),
            ("unit", "unit", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetailSubDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("quantity", "quantity", Quantity, False, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItemDetail(BackboneElement):
    """ Insurer added line items.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    quantity: Optional[Quantity] = None
    subDetail: Optional[List[ExplanationOfBenefitAddItemDetailSubDetail]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("quantity", "quantity", Quantity, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItem"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    detail: Optional[List[ExplanationOfBenefitAddItemDetail]] = empty_list()
    detailSequence: Optional[List[int]] = empty_list()
    factor: Optional[float] = None
    itemSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[Address] = None
    locationCodeableConcept: Optional[CodeableConcept] = None
    locationReference: Optional[FHIRReference] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    programCode: Optional[List[CodeableConcept]] = empty_list()
    provider: Optional[List[FHIRReference]] = empty_list()
    quantity: Optional[Quantity] = None
    servicedDate: Optional[FHIRDate] = None
    servicedPeriod: Optional[Period] = None
    subDetailSequence: Optional[List[int]] = empty_list()
    subSite: Optional[List[CodeableConcept]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("programCode", "programCode", CodeableConcept, True, None, False),
            ("provider", "provider", FHIRReference, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("servicedDate", "servicedDate", FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", Period, False, "serviced", False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("subSite", "subSite", CodeableConcept, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefitAccident(BackboneElement):
    """ Details of the event.

    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAccident"
    date: Optional[FHIRDate] = None
    locationAddress: Optional[Address] = None
    locationReference: Optional[FHIRReference] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", FHIRDate, False, None, False),
            ("locationAddress", "locationAddress", Address, False, "location", False),
            ("locationReference", "locationReference", FHIRReference, False, "location", False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class ExplanationOfBenefit(DomainResource):
    """ Explanation of Benefit resource.

    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefit"
    accident: Optional[ExplanationOfBenefitAccident] = None
    addItem: Optional[List[ExplanationOfBenefitAddItem]] = empty_list()
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    benefitBalance: Optional[List[ExplanationOfBenefitBenefitBalance]] = empty_list()
    benefitPeriod: Optional[Period] = None
    billablePeriod: Optional[Period] = None
    careTeam: Optional[List[ExplanationOfBenefitCareTeam]] = empty_list()
    claim: Optional[FHIRReference] = None
    claimResponse: Optional[FHIRReference] = None
    created: FHIRDate = None
    diagnosis: Optional[List[ExplanationOfBenefitDiagnosis]] = empty_list()
    disposition: Optional[str] = None
    enterer: Optional[FHIRReference] = None
    facility: Optional[FHIRReference] = None
    form: Optional[Attachment] = None
    formCode: Optional[CodeableConcept] = None
    fundsReserve: Optional[CodeableConcept] = None
    fundsReserveRequested: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurance: List[ExplanationOfBenefitInsurance] = empty_list()
    insurer: FHIRReference = None
    item: Optional[List[ExplanationOfBenefitItem]] = empty_list()
    originalPrescription: Optional[FHIRReference] = None
    outcome: str = None
    patient: FHIRReference = None
    payee: Optional[ExplanationOfBenefitPayee] = None
    payment: Optional[ExplanationOfBenefitPayment] = None
    preAuthRef: Optional[List[str]] = empty_list()
    preAuthRefPeriod: Optional[List[Period]] = empty_list()
    precedence: Optional[int] = None
    prescription: Optional[FHIRReference] = None
    priority: Optional[CodeableConcept] = None
    procedure: Optional[List[ExplanationOfBenefitProcedure]] = empty_list()
    processNote: Optional[List[ExplanationOfBenefitProcessNote]] = empty_list()
    provider: FHIRReference = None
    referral: Optional[FHIRReference] = None
    related: Optional[List[ExplanationOfBenefitRelated]] = empty_list()
    status: str = None
    subType: Optional[CodeableConcept] = None
    supportingInfo: Optional[List[ExplanationOfBenefitSupportingInfo]] = empty_list()
    total: Optional[List[ExplanationOfBenefitTotal]] = empty_list()
    type: CodeableConcept = None
    use: str = None

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("benefitPeriod", "benefitPeriod", Period, False, None, False),
            ("billablePeriod", "billablePeriod", Period, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("claim", "claim", FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("enterer", "enterer", FHIRReference, False, None, False),
            ("facility", "facility", FHIRReference, False, None, False),
            ("form", "form", Attachment, False, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("fundsReserveRequested", "fundsReserveRequested", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, True),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("originalPrescription", "originalPrescription", FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("preAuthRefPeriod", "preAuthRefPeriod", Period, True, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("prescription", "prescription", FHIRReference, False, None, False),
            ("priority", "priority", CodeableConcept, False, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("provider", "provider", FHIRReference, False, None, True),
            ("referral", "referral", FHIRReference, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, True, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js