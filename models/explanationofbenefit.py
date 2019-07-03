#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2019-07-03.
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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.accident = None
#        """ Details of the event.
#        Type `ExplanationOfBenefitAccident`
#
# (represented as `dict` in JSON). """
#
#
#        self.addItem = None
#        """ Insurer added line items.
#        List of `ExplanationOfBenefitAddItem` items
#
# (represented as `dict` in JSON). """
#
#
#        self.adjudication = None
#        """ Header-level adjudication.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.benefitBalance = None
#        """ Balance by Benefit Category.
#        List of `ExplanationOfBenefitBenefitBalance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.benefitPeriod = None
#        """ When the benefits are applicable.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.billablePeriod = None
#        """ Relevant time frame for the claim.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.careTeam = None
#        """ Care Team members.
#        List of `ExplanationOfBenefitCareTeam` items
#
# (represented as `dict` in JSON). """
#
#
#        self.claim = None
#        """ Claim reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.claimResponse = None
#        """ Claim response reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.created = None
#        """ Response creation date.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.diagnosis = None
#        """ Pertinent diagnosis information.
#        List of `ExplanationOfBenefitDiagnosis` items
#
# (represented as `dict` in JSON). """
#
#
#        self.disposition = None
#        """ Disposition Message.
#        Type `str`
#
#. """
#
#
#        self.enterer = None
#        """ Author of the claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.facility = None
#        """ Servicing Facility.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.form = None
#        """ Printed reference or actual form.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.formCode = None
#        """ Printed form identifier.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.fundsReserve = None
#        """ Funds reserved status.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.fundsReserveRequested = None
#        """ For whom to reserve funds.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business Identifier for the resource.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.insurance = None
#        """ Patient insurance information.
#        List of `ExplanationOfBenefitInsurance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.insurer = None
#        """ Party responsible for reimbursement.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.item = None
#        """ Product or service provided.
#        List of `ExplanationOfBenefitItem` items
#
# (represented as `dict` in JSON). """
#
#
#        self.originalPrescription = None
#        """ Original prescription if superceded by fulfiller.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.outcome = None
#        """ queued | complete | error | partial.
#        Type `str`
#
#. """
#
#
#        self.patient = None
#        """ The recipient of the products and services.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.payee = None
#        """ Recipient of benefits payable.
#        Type `ExplanationOfBenefitPayee`
#
# (represented as `dict` in JSON). """
#
#
#        self.payment = None
#        """ Payment Details.
#        Type `ExplanationOfBenefitPayment`
#
# (represented as `dict` in JSON). """
#
#
#        self.preAuthRef = None
#        """ Preauthorization reference.
#        List of `str` items
#
#. """
#
#
#        self.preAuthRefPeriod = None
#        """ Preauthorization in-effect period.
#        List of `Period` items
#
# (represented as `dict` in JSON). """
#
#
#        self.precedence = None
#        """ Precedence (primary, secondary, etc.).
#        Type `int`
#
#. """
#
#
#        self.prescription = None
#        """ Prescription authorizing services or products.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.priority = None
#        """ Desired processing urgency.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.procedure = None
#        """ Clinical procedures performed.
#        List of `ExplanationOfBenefitProcedure` items
#
# (represented as `dict` in JSON). """
#
#
#        self.processNote = None
#        """ Note concerning adjudication.
#        List of `ExplanationOfBenefitProcessNote` items
#
# (represented as `dict` in JSON). """
#
#
#        self.provider = None
#        """ Party responsible for the claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.referral = None
#        """ Treatment Referral.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.related = None
#        """ Prior or corollary claims.
#        List of `ExplanationOfBenefitRelated` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | cancelled | draft | entered-in-error.
#        Type `str`
#
#. """
#
#
#        self.subType = None
#        """ More granular claim type.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.supportingInfo = None
#        """ Supporting information.
#        List of `ExplanationOfBenefitSupportingInfo` items
#
# (represented as `dict` in JSON). """
#
#
#        self.total = None
#        """ Adjudication totals.
#        List of `ExplanationOfBenefitTotal` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Category or discipline.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.use = None
#        """ claim | preauthorization | predetermination.
#        Type `str`
#
#. """
#

#        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, {  # #}False, None, {  # #}False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, {  # #}True, None, {  # #}False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, {  # #}True, None, {  # #}False),
            ("benefitPeriod", "benefitPeriod", period.Period, {  # #}False, None, {  # #}False),
            ("billablePeriod", "billablePeriod", period.Period, {  # #}False, None, {  # #}False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, {  # #}True, None, {  # #}False),
            ("claim", "claim", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("created", "created", fhirdate.FHIRDate, {  # #}False, None, {  # #}True),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, {  # #}True, None, {  # #}False),
            ("disposition", "disposition", str, {  # #}False, None, {  # #}False),
            ("enterer", "enterer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("facility", "facility", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("form", "form", attachment.Attachment, {  # #}False, None, {  # #}False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("fundsReserveRequested", "fundsReserveRequested", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, {  # #}True, None, {  # #}True),
            ("insurer", "insurer", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("item", "item", ExplanationOfBenefitItem, {  # #}True, None, {  # #}False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("outcome", "outcome", str, {  # #}False, None, {  # #}True),
            ("patient", "patient", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("payee", "payee", ExplanationOfBenefitPayee, {  # #}False, None, {  # #}False),
            ("payment", "payment", ExplanationOfBenefitPayment, {  # #}False, None, {  # #}False),
            ("preAuthRef", "preAuthRef", str, {  # #}True, None, {  # #}False),
            ("preAuthRefPeriod", "preAuthRefPeriod", period.Period, {  # #}True, None, {  # #}False),
            ("precedence", "precedence", int, {  # #}False, None, {  # #}False),
            ("prescription", "prescription", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("priority", "priority", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, {  # #}True, None, {  # #}False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, {  # #}True, None, {  # #}False),
            ("provider", "provider", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("referral", "referral", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("related", "related", ExplanationOfBenefitRelated, {  # #}True, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subType", "subType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, {  # #}True, None, {  # #}False),
            ("total", "total", ExplanationOfBenefitTotal, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("use", "use", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.date = None
#        """ When the incident occurred.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.locationAddress = None
#        """ Where the event occurred.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Where the event occurred.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ The nature of the accident.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitAccident, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("locationAddress", "locationAddress", address.Address, {  # #}False, "location", {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}False, "location", {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Added items adjudication.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.bodySite = None
#        """ Anatomical location.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.detail = None
#        """ Insurer added line items.
#        List of `ExplanationOfBenefitAddItemDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.detailSequence = None
#        """ Detail sequence number.
#        List of `int` items
#
#. """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.itemSequence = None
#        """ Item sequence number.
#        List of `int` items
#
#. """
#
#
#        self.locationAddress = None
#        """ Place of service or where product was supplied.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationCodeableConcept = None
#        """ Place of service or where product was supplied.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Place of service or where product was supplied.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.provider = None
#        """ Authorized providers.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.servicedDate = None
#        """ Date or dates of service or product delivery.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.servicedPeriod = None
#        """ Date or dates of service or product delivery.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.subDetailSequence = None
#        """ Subdetail sequence number.
#        List of `int` items
#
#. """
#
#
#        self.subSite = None
#        """ Anatomical sub-location.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitAddItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, {  # #}True, None, {  # #}False),
            ("detailSequence", "detailSequence", int, {  # #}True, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("itemSequence", "itemSequence", int, {  # #}True, None, {  # #}False),
            ("locationAddress", "locationAddress", address.Address, {  # #}False, "location", {  # #}False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "location", {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}False, "location", {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("provider", "provider", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, {  # #}False, "serviced", {  # #}False),
            ("servicedPeriod", "servicedPeriod", period.Period, {  # #}False, "serviced", {  # #}False),
            ("subDetailSequence", "subDetailSequence", int, {  # #}True, None, {  # #}False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Added items adjudication.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.subDetail = None
#        """ Insurer added line items.
#        List of `ExplanationOfBenefitAddItemDetailSubDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Added items adjudication.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Description of the benefit or services covered.
#        Type `str`
#
#. """
#
#
#        self.excluded = None
#        """ Excluded from the plan.
#        Type `bool`
#
#. """
#
#
#        self.financial = None
#        """ Benefit Summary.
#        List of `ExplanationOfBenefitBenefitBalanceFinancial` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Short name for the benefit.
#        Type `str`
#
#. """
#
#
#        self.network = None
#        """ In or out of network.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.term = None
#        """ Annual or lifetime.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.unit = None
#        """ Individual or family.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("excluded", "excluded", bool, {  # #}False, None, {  # #}False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("network", "network", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("term", "term", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("unit", "unit", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.allowedMoney = None
#        """ Benefits allowed.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.allowedString = None
#        """ Benefits allowed.
#        Type `str`
#
#. """
#
#
#        self.allowedUnsignedInt = None
#        """ Benefits allowed.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.usedMoney = None
#        """ Benefits used.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.usedUnsignedInt = None
#        """ Benefits used.
#        Type `int`
#
#. """
#

#        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, {  # #}False, "allowed", {  # #}False),
            ("allowedString", "allowedString", str, {  # #}False, "allowed", {  # #}False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, {  # #}False, "allowed", {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("usedMoney", "usedMoney", money.Money, {  # #}False, "used", {  # #}False),
            ("usedUnsignedInt", "usedUnsignedInt", int, {  # #}False, "used", {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.provider = None
#        """ Practitioner or organization.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.qualification = None
#        """ Practitioner credential or specialization.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.responsible = None
#        """ Indicator of the lead practitioner.
#        Type `bool`
#
#. """
#
#
#        self.role = None
#        """ Function within the team.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Order of care team.
#        Type `int`
#
#. """
#

#        super(ExplanationOfBenefitCareTeam, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("responsible", "responsible", bool, {  # #}False, None, {  # #}False),
            ("role", "role", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.diagnosisCodeableConcept = None
#        """ Nature of illness or problem.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.diagnosisReference = None
#        """ Nature of illness or problem.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.onAdmission = None
#        """ Present on admission.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.packageCode = None
#        """ Package billing code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Diagnosis instance identifier.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Timing or nature of the diagnosis.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "diagnosis", {  # #}True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, {  # #}False, "diagnosis", {  # #}True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.coverage = None
#        """ Insurance information.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.focal = None
#        """ Coverage to be used for adjudication.
#        Type `bool`
#
#. """
#
#
#        self.preAuthRef = None
#        """ Prior authorization reference number.
#        List of `str` items
#
#. """
#

#        super(ExplanationOfBenefitInsurance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("focal", "focal", bool, {  # #}False, None, {  # #}True),
            ("preAuthRef", "preAuthRef", str, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Adjudication details.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.bodySite = None
#        """ Anatomical location.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.careTeamSequence = None
#        """ Applicable care team members.
#        List of `int` items
#
#. """
#
#
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.detail = None
#        """ Additional items.
#        List of `ExplanationOfBenefitItemDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.diagnosisSequence = None
#        """ Applicable diagnoses.
#        List of `int` items
#
#. """
#
#
#        self.encounter = None
#        """ Encounters related to this billed item.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.informationSequence = None
#        """ Applicable exception and supporting information.
#        List of `int` items
#
#. """
#
#
#        self.locationAddress = None
#        """ Place of service or where product was supplied.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationCodeableConcept = None
#        """ Place of service or where product was supplied.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.locationReference = None
#        """ Place of service or where product was supplied.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.modifier = None
#        """ Product or service billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.procedureSequence = None
#        """ Applicable procedures.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Item instance identifier.
#        Type `int`
#
#. """
#
#
#        self.servicedDate = None
#        """ Date or dates of service or product delivery.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.servicedPeriod = None
#        """ Date or dates of service or product delivery.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.subSite = None
#        """ Anatomical sub-location.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("careTeamSequence", "careTeamSequence", int, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, {  # #}True, None, {  # #}False),
            ("diagnosisSequence", "diagnosisSequence", int, {  # #}True, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("informationSequence", "informationSequence", int, {  # #}True, None, {  # #}False),
            ("locationAddress", "locationAddress", address.Address, {  # #}False, "location", {  # #}False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "location", {  # #}False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, {  # #}False, "location", {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("procedureSequence", "procedureSequence", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, {  # #}False, "serviced", {  # #}False),
            ("servicedPeriod", "servicedPeriod", period.Period, {  # #}False, "serviced", {  # #}False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.amount = None
#        """ Monetary amount.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Type of adjudication information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.reason = None
#        """ Explanation of adjudication outcome.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.value = None
#        """ Non-monitary value.
#        Type `float`
#
#. """
#

#        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, {  # #}False, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("reason", "reason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("value", "value", float, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Detail level adjudication details.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Product or service provided.
#        Type `int`
#
#. """
#
#
#        self.subDetail = None
#        """ Additional items.
#        List of `ExplanationOfBenefitItemDetailSubDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjudication = None
#        """ Subdetail level adjudication details.
#        List of `ExplanationOfBenefitItemAdjudication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Benefit classification.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.factor = None
#        """ Price scaling factor.
#        Type `float`
#
#. """
#
#
#        self.modifier = None
#        """ Service/Product billing modifiers.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.net = None
#        """ Total item cost.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.noteNumber = None
#        """ Applicable note numbers.
#        List of `int` items
#
#. """
#
#
#        self.productOrService = None
#        """ Billing, service, product, or drug code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.programCode = None
#        """ Program the product or service is provided under.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ Count of products or services.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.revenue = None
#        """ Revenue or cost center code.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Product or service provided.
#        Type `int`
#
#. """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.unitPrice = None
#        """ Fee, charge or cost per item.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, {  # #}True, None, {  # #}False),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("factor", "factor", float, {  # #}False, None, {  # #}False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("net", "net", money.Money, {  # #}False, None, {  # #}False),
            ("noteNumber", "noteNumber", int, {  # #}True, None, {  # #}False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("unitPrice", "unitPrice", money.Money, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.party = None
#        """ Recipient reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Category of recipient.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitPayee, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.adjustment = None
#        """ Payment adjustment for non-claim issues.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.adjustmentReason = None
#        """ Explanation for the variance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.amount = None
#        """ Payable amount after adjustment.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Expected date of payment.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier for the payment.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Partial or complete payment.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitPayment, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, {  # #}False, None, {  # #}False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("amount", "amount", money.Money, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.date = None
#        """ When the procedure was performed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.procedureCodeableConcept = None
#        """ Specific clinical procedure.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.procedureReference = None
#        """ Specific clinical procedure.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Procedure instance identifier.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Category of Procedure.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.udi = None
#        """ Unique device identifier.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitProcedure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "procedure", {  # #}True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, {  # #}False, "procedure", {  # #}True),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("udi", "udi", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.language = None
#        """ Language of the text.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.number = None
#        """ Note instance identifier.
#        Type `int`
#
#. """
#
#
#        self.text = None
#        """ Note explanatory text.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ display | print | printoper.
#        Type `str`
#
#. """
#

#        super(ExplanationOfBenefitProcessNote, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("number", "number", int, {  # #}False, None, {  # #}False),
            ("text", "text", str, {  # #}False, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.claim = None
#        """ Reference to the related claim.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.reference = None
#        """ File or case reference.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ How the reference claim is related.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitRelated, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("reference", "reference", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.category = None
#        """ Classification of the supplied information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Type of information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.reason = None
#        """ Explanation for the information.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.sequence = None
#        """ Information instance identifier.
#        Type `int`
#
#. """
#
#
#        self.timingDate = None
#        """ When it occurred.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.timingPeriod = None
#        """ When it occurred.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueAttachment = None
#        """ Data to be provided.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueBoolean = None
#        """ Data to be provided.
#        Type `bool`
#
#. """
#
#
#        self.valueQuantity = None
#        """ Data to be provided.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueReference = None
#        """ Data to be provided.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueString = None
#        """ Data to be provided.
#        Type `str`
#
#. """
#

#        super(ExplanationOfBenefitSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("reason", "reason", coding.Coding, {  # #}False, None, {  # #}False),
            ("sequence", "sequence", int, {  # #}False, None, {  # #}True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, {  # #}False, "timing", {  # #}False),
            ("timingPeriod", "timingPeriod", period.Period, {  # #}False, "timing", {  # #}False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, {  # #}False, "value", {  # #}False),
            ("valueBoolean", "valueBoolean", bool, {  # #}False, "value", {  # #}False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, {  # #}False, "value", {  # #}False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, {  # #}False, "value", {  # #}False),
            ("valueString", "valueString", str, {  # #}False, "value", {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity


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

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.amount = None
#        """ Financial total for the category.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.category = None
#        """ Type of adjudication information.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ExplanationOfBenefitTotal, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, {  # #}False, None, {  # #}True),
            ("category", "category", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js