#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity

from . import domainresource

@dataclass
class ExplanationOfBenefit(domainresource.DomainResource):
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
    benefitPeriod: Optional[period.Period] = None
    billablePeriod: Optional[period.Period] = None
    careTeam: Optional[List[ExplanationOfBenefitCareTeam]] = empty_list()
    claim: Optional[fhirreference.FHIRReference] = None
    claimResponse: Optional[fhirreference.FHIRReference] = None
    created:fhirdate.FHIRDate = None
    diagnosis: Optional[List[ExplanationOfBenefitDiagnosis]] = empty_list()
    disposition: Optional[str] = None
    enterer: Optional[fhirreference.FHIRReference] = None
    facility: Optional[fhirreference.FHIRReference] = None
    form: Optional[attachment.Attachment] = None
    formCode: Optional[codeableconcept.CodeableConcept] = None
    fundsReserve: Optional[codeableconcept.CodeableConcept] = None
    fundsReserveRequested: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    insurance: List[ ExplanationOfBenefitInsurance] = empty_list()
    insurer:fhirreference.FHIRReference = None
    item: Optional[List[ExplanationOfBenefitItem]] = empty_list()
    originalPrescription: Optional[fhirreference.FHIRReference] = None
    outcome: str = None
    patient:fhirreference.FHIRReference = None
    payee: Optional[ExplanationOfBenefitPayee] = None
    payment: Optional[ExplanationOfBenefitPayment] = None
    preAuthRef: Optional[List[str]] = empty_list()
    preAuthRefPeriod: Optional[List[period.Period]] = empty_list()
    precedence: Optional[int] = None
    prescription: Optional[fhirreference.FHIRReference] = None
    priority: Optional[codeableconcept.CodeableConcept] = None
    procedure: Optional[List[ExplanationOfBenefitProcedure]] = empty_list()
    processNote: Optional[List[ExplanationOfBenefitProcessNote]] = empty_list()
    provider:fhirreference.FHIRReference = None
    referral: Optional[fhirreference.FHIRReference] = None
    related: Optional[List[ExplanationOfBenefitRelated]] = empty_list()
    status: str = None
    subType: Optional[codeableconcept.CodeableConcept] = None
    supportingInfo: Optional[List[ExplanationOfBenefitSupportingInfo]] = empty_list()
    total: Optional[List[ExplanationOfBenefitTotal]] = empty_list()
    type:codeableconcept.CodeableConcept = None
    use: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserveRequested", "fundsReserveRequested", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, True),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("preAuthRefPeriod", "preAuthRefPeriod", period.Period, True, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, True, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of the event.

    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAccident"
    date: Optional[fhirdate.FHIRDate] = None
    locationAddress: Optional[address.Address] = None
    locationReference: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItem"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[List[ExplanationOfBenefitAddItemDetail]] = empty_list()
    detailSequence: Optional[List[int]] = empty_list()
    factor: Optional[float] = None
    itemSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[address.Address] = None
    locationCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    locationReference: Optional[fhirreference.FHIRReference] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    provider: Optional[List[fhirreference.FHIRReference]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    servicedDate: Optional[fhirdate.FHIRDate] = None
    servicedPeriod: Optional[period.Period] = None
    subDetailSequence: Optional[List[int]] = empty_list()
    subSite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    quantity: Optional[quantity.Quantity] = None
    subDetail: Optional[List[ExplanationOfBenefitAddItemDetailSubDetail]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitAddItemDetailSubDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    quantity: Optional[quantity.Quantity] = None
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalance"
    category:codeableconcept.CodeableConcept = None
    description: Optional[str] = None
    excluded: Optional[bool] = None
    financial: Optional[List[ExplanationOfBenefitBenefitBalanceFinancial]] = empty_list()
    name: Optional[str] = None
    network: Optional[codeableconcept.CodeableConcept] = None
    term: Optional[codeableconcept.CodeableConcept] = None
    unit: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.

    Benefits Used to date.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitBenefitBalanceFinancial"
    allowedMoney: Optional[money.Money] = None
    allowedString: Optional[str] = None
    allowedUnsignedInt: Optional[int] = None
    type:codeableconcept.CodeableConcept = None
    usedMoney: Optional[money.Money] = None
    usedUnsignedInt: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
        ])
        return js

@dataclass
class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """ Care Team members.

    The members of the team who provided the products and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitCareTeam"
    provider:fhirreference.FHIRReference = None
    qualification: Optional[codeableconcept.CodeableConcept] = None
    responsible: Optional[bool] = None
    role: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js

@dataclass
class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.

    Information about diagnoses relevant to the claim items.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitDiagnosis"
    diagnosisCodeableConcept:codeableconcept.CodeableConcept = None
    diagnosisReference:fhirreference.FHIRReference = None
    onAdmission: Optional[codeableconcept.CodeableConcept] = None
    packageCode: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitInsurance"
    coverage:fhirreference.FHIRReference = None
    focal: bool = None
    preAuthRef: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Product or service provided.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItem"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    careTeamSequence: Optional[List[int]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[List[ExplanationOfBenefitItemDetail]] = empty_list()
    diagnosisSequence: Optional[List[int]] = empty_list()
    encounter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    factor: Optional[float] = None
    informationSequence: Optional[List[int]] = empty_list()
    locationAddress: Optional[address.Address] = None
    locationCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    locationReference: Optional[fhirreference.FHIRReference] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    procedureSequence: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    servicedDate: Optional[fhirdate.FHIRDate] = None
    servicedPeriod: Optional[period.Period] = None
    subSite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemAdjudication"
    amount: Optional[money.Money] = None
    category:codeableconcept.CodeableConcept = None
    reason: Optional[codeableconcept.CodeableConcept] = None
    value: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.

    Second-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    subDetail: Optional[List[ExplanationOfBenefitItemDetailSubDetail]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.

    Third-tier of goods and services.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitItemDetailSubDetail"
    adjudication: Optional[List[ExplanationOfBenefitItemAdjudication]] = empty_list()
    category: Optional[codeableconcept.CodeableConcept] = None
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    programCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    revenue: Optional[codeableconcept.CodeableConcept] = None
    sequence: int = None
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.

    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayee"
    party: Optional[fhirreference.FHIRReference] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitPayment"
    adjustment: Optional[money.Money] = None
    adjustmentReason: Optional[codeableconcept.CodeableConcept] = None
    amount: Optional[money.Money] = None
    date: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[identifier.Identifier] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.

    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcedure"
    date: Optional[fhirdate.FHIRDate] = None
    procedureCodeableConcept:codeableconcept.CodeableConcept = None
    procedureReference:fhirreference.FHIRReference = None
    sequence: int = None
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    udi: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitProcessNote"
    language: Optional[codeableconcept.CodeableConcept] = None
    number: Optional[int] = None
    text: Optional[str] = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.

    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitRelated"
    claim: Optional[fhirreference.FHIRReference] = None
    reference: Optional[identifier.Identifier] = None
    relationship: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.

    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitSupportingInfo"
    category:codeableconcept.CodeableConcept = None
    code: Optional[codeableconcept.CodeableConcept] = None
    reason: Optional[coding.Coding] = None
    sequence: int = None
    timingDate: Optional[fhirdate.FHIRDate] = None
    timingPeriod: Optional[period.Period] = None
    valueAttachment: Optional[attachment.Attachment] = None
    valueBoolean: Optional[bool] = None
    valueQuantity: Optional[quantity.Quantity] = None
    valueReference: Optional[fhirreference.FHIRReference] = None
    valueString: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js

@dataclass
class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ExplanationOfBenefitTotal"
    amount:money.Money = None
    category:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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