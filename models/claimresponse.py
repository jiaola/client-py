#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity

from . import backboneelement

@dataclass
class ClaimResponseTotal(backboneelement.BackboneElement):
    """ Adjudication totals.

    Categorized monetary totals for the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseTotal"
    amount:money.Money = None
    category:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.

    A note that describes or explains adjudication results in a human readable
    form.
    """
    resource_type: ClassVar[str] = "ClaimResponseProcessNote"
    language: Optional[codeableconcept.CodeableConcept] = None
    number: Optional[int] = None
    text: str = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class ClaimResponsePayment(backboneelement.BackboneElement):
    """ Payment Details.

    Payment details for the adjudication of the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponsePayment"
    adjustment: Optional[money.Money] = None
    adjustmentReason: Optional[codeableconcept.CodeableConcept] = None
    amount:money.Money = None
    date: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[identifier.Identifier] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Adjudication for claim sub-details.

    A sub-detail adjudication of a simple product or service.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetailSubDetail"
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = empty_list()
    noteNumber: Optional[List[int]] = empty_list()
    subDetailSequence: int = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, True),
        ])
        return js

@dataclass
class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Adjudication for claim details.

    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemDetail"
    adjudication: List[ ClaimResponseItemAdjudication] = empty_list()
    detailSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()
    subDetail: Optional[List[ClaimResponseItemDetailSubDetail]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

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
class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.

    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    resource_type: ClassVar[str] = "ClaimResponseItemAdjudication"
    amount: Optional[money.Money] = None
    category:codeableconcept.CodeableConcept = None
    reason: Optional[codeableconcept.CodeableConcept] = None
    value: Optional[float] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js

@dataclass
class ClaimResponseItem(backboneelement.BackboneElement):
    """ Adjudication for claim line items.

    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    resource_type: ClassVar[str] = "ClaimResponseItem"
    adjudication: List[ ClaimResponseItemAdjudication] = empty_list()
    detail: Optional[List[ClaimResponseItemDetail]] = empty_list()
    itemSequence: int = None
    noteNumber: Optional[List[int]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

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
class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.

    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    resource_type: ClassVar[str] = "ClaimResponseInsurance"
    businessArrangement: Optional[str] = None
    claimResponse: Optional[fhirreference.FHIRReference] = None
    coverage:fhirreference.FHIRReference = None
    focal: bool = None
    sequence: int = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js

@dataclass
class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.

    Errors encountered during the processing of the adjudication.
    """
    resource_type: ClassVar[str] = "ClaimResponseError"
    code:codeableconcept.CodeableConcept = None
    detailSequence: Optional[int] = None
    itemSequence: Optional[int] = None
    subDetailSequence: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("detailSequence", "detailSequence", int, False, None, False),
            ("itemSequence", "itemSequence", int, False, None, False),
            ("subDetailSequence", "subDetailSequence", int, False, None, False),
        ])
        return js

@dataclass
class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.

    The third-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetailSubDetail"
    adjudication: List[ ClaimResponseItemAdjudication] = empty_list()
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
        js = super(ClaimResponseAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
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
class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line details.

    The second-tier service adjudications for payor added services.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItemDetail"
    adjudication: List[ ClaimResponseItemAdjudication] = empty_list()
    factor: Optional[float] = None
    modifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    net: Optional[money.Money] = None
    noteNumber: Optional[List[int]] = empty_list()
    productOrService:codeableconcept.CodeableConcept = None
    quantity: Optional[quantity.Quantity] = None
    subDetail: Optional[List[ClaimResponseAddItemDetailSubDetail]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ClaimResponseAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

@dataclass
class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.

    The first-tier service adjudications for payor added product or service
    lines.
    """
    resource_type: ClassVar[str] = "ClaimResponseAddItem"
    adjudication: List[ ClaimResponseItemAdjudication] = empty_list()
    bodySite: Optional[codeableconcept.CodeableConcept] = None
    detail: Optional[List[ClaimResponseAddItemDetail]] = empty_list()
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
    subSite: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    subdetailSequence: Optional[List[int]] = empty_list()
    unitPrice: Optional[money.Money] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, True),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
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
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("subdetailSequence", "subdetailSequence", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class ClaimResponse(domainresource.DomainResource):
    """ Response to a claim predetermination or preauthorization.

    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    resource_type: ClassVar[str] = "ClaimResponse"
    addItem: Optional[List[ClaimResponseAddItem]] = empty_list()
    adjudication: Optional[List[ClaimResponseItemAdjudication]] = empty_list()
    communicationRequest: Optional[List[fhirreference.FHIRReference]] = empty_list()
    created:fhirdate.FHIRDate = None
    disposition: Optional[str] = None
    error: Optional[List[ClaimResponseError]] = empty_list()
    form: Optional[attachment.Attachment] = None
    formCode: Optional[codeableconcept.CodeableConcept] = None
    fundsReserve: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    insurance: Optional[List[ClaimResponseInsurance]] = empty_list()
    insurer:fhirreference.FHIRReference = None
    item: Optional[List[ClaimResponseItem]] = empty_list()
    outcome: str = None
    patient:fhirreference.FHIRReference = None
    payeeType: Optional[codeableconcept.CodeableConcept] = None
    payment: Optional[ClaimResponsePayment] = None
    preAuthPeriod: Optional[period.Period] = None
    preAuthRef: Optional[str] = None
    processNote: Optional[List[ClaimResponseProcessNote]] = empty_list()
    request: Optional[fhirreference.FHIRReference] = None
    requestor: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subType: Optional[codeableconcept.CodeableConcept] = None
    total: Optional[List[ClaimResponseTotal]] = empty_list()
    type:codeableconcept.CodeableConcept = None
    use: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payeeType", "payeeType", codeableconcept.CodeableConcept, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("preAuthPeriod", "preAuthPeriod", period.Period, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("total", "total", ClaimResponseTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
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