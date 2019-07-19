#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2019-07-18.
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
class ClaimResponseTotal(BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseTotal"
    amount: Money = None
    category: CodeableConcept = None

    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, True),
            ("category", "category", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ClaimResponseProcessNote(BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ClaimResponseProcessNote"
    language: Optional[CodeableConcept] = None
    number: Optional[int] = None
    text: str = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class ClaimResponsePayment(BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponsePayment"
    adjustment: Optional[Money] = None
    adjustmentReason: Optional[CodeableConcept] = None
    amount: Money = None
    date: Optional[FHIRDate] = None
    identifier: Optional[Identifier] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", CodeableConcept, False, None, False),
            ("amount", "amount", Money, False, None, True),
            ("date", "date", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class ClaimResponseItemDetailSubDetail(BackboneElement):
    """ Adjudication for claim sub-details.

    A sub-detail adjudication of a simple product or service.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetailSubDetail"
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = empty_list()
    noteNumber: Optional[List[int]] = empty_list()
    subDetailSequence: int = None

    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
        ])
        return js


@dataclass
class ClaimResponseItemDetail(BackboneElement):
    """ Adjudication for claim details.

    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetail"
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    detailSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()
    subDetail: Optional[List[ClaimResponseItemDetailSubDetail]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detailSequence", "detailSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseItemAdjudication(BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemAdjudication"
    amount: Optional[Money] = None
    category: CodeableConcept = None
    reason: Optional[CodeableConcept] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, False),
            ("category", "category", CodeableConcept, False, None, True),
            ("reason", "reason", CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseItem(BackboneElement):
    """ Adjudication for claim line items.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimResponseItem"
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    detail: Optional[List[ClaimResponseItemDetail]] = empty_list()
    itemSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()

    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
            ("itemSequence", "itemSequence", int, False, None, True),
            ("noteNumber", "noteNumber", int, True, None, False),
        ])
        return js


@dataclass
class ClaimResponseInsurance(BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponseInsurance"
    businessArrangement: Optional[str] = None
    claimResponse: Optional[FHIRReference] = None
    coverage: FHIRReference = None
    focal: bool = None
    sequence: int = None

    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", FHIRReference, False, None, False),
            ("coverage", "coverage", FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


@dataclass
class ClaimResponseError(BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseError"
    code: CodeableConcept = None
    detailSequence: Optional[int] = None
    itemSequence: Optional[int] = None
    subDetailSequence: Optional[int] = None

    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseAddItemDetailSubDetail(BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetailSubDetail"
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    quantity: Optional[Quantity] = None
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
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
class ClaimResponseAddItemDetail(BackboneElement):
    """ Insurer added line details.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetail"
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[CodeableConcept]] = empty_list()
    net: Optional[Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService: CodeableConcept = None
    quantity: Optional[Quantity] = None
    subDetail: Optional[List[ClaimResponseAddItemDetailSubDetail]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", CodeableConcept, True, None, False),
            ("net", "net", Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", CodeableConcept, False, None, True),
            ("quantity", "quantity", Quantity, False, None, False),
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ClaimResponseAddItem(BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItem"
    adjudication: List[ClaimResponseItemAdjudication] = empty_list()
    bodySite: Optional[CodeableConcept] = None
    detail: Optional[List[ClaimResponseAddItemDetail]] = empty_list()
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
    subSite: Optional[List[CodeableConcept]] = empty_list()
    subdetailSequence: Optional[List[int]] = empty_list()
    unitPrice: Optional[Money] = None

    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("bodySite", "bodySite", CodeableConcept, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
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
            ("subSite", "subSite", CodeableConcept, True, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
            ("unitPrice", "unitPrice", Money, False, None, False),
        ])
        return js


@dataclass
class ClaimResponse(DomainResource):
    """ Response to a claim predetermination or preauthorization.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    resource_type: ClassVar[str] = "ClaimResponse"
    addItem: Optional[List[ClaimResponseAddItem]] = empty_list()
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = empty_list()
    communicationRequest: Optional[List[FHIRReference]] = empty_list()
    created: FHIRDate = None
    disposition: Optional[str] = None
    error: Optional[List[ClaimResponseError]] = empty_list()
    form: Optional[Attachment] = None
    formCode: Optional[CodeableConcept] = None
    fundsReserve: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    insurance: Optional[List[ClaimResponseInsurance]] = empty_list()
    insurer: FHIRReference = None
    item: Optional[List[ClaimResponseItem]] = empty_list()
    outcome: str = None
    patient: FHIRReference = None
    payeeType: Optional[CodeableConcept] = None
    payment: Optional[ClaimResponsePayment] = None
    preAuthPeriod: Optional[Period] = None
    preAuthRef: Optional[str] = None
    processNote: Optional[List[ClaimResponseProcessNote]] = empty_list()
    request: Optional[FHIRReference] = None
    requestor: Optional[FHIRReference] = None
    status: str = None
    subType: Optional[CodeableConcept] = None
    total: Optional[List[ClaimResponseTotal]] = empty_list()
    type: CodeableConcept = None
    use: str = None

    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("communicationRequest", "communicationRequest", FHIRReference, True, None, False),
            ("created", "created", FHIRDate, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("form", "form", Attachment, False, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("insurer", "insurer", FHIRReference, False, None, True),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", FHIRReference, False, None, True),
            ("payeeType", "payeeType", CodeableConcept, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("preAuthPeriod", "preAuthPeriod", Period, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", CodeableConcept, False, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js