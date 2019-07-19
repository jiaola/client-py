#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Invoice) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money


@dataclass
class InvoiceParticipant(BackboneElement):
    """ Participant in creation of this Invoice.

    Indicates who or what performed or participated in the charged service.
    """
    resource_type: ClassVar[str] = "InvoiceParticipant"
    actor: FHIRReference = None
    role: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", FHIRReference, False, None, True),
            ("role", "role", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class InvoiceLineItemPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "InvoiceLineItemPriceComponent"
    amount: Optional[Money] = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    type: str = None

    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class InvoiceLineItem(BackboneElement):
    """ Line items of this Invoice.

    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    resource_type: ClassVar[str] = "InvoiceLineItem"
    chargeItemCodeableConcept: CodeableConcept = None
    chargeItemReference: FHIRReference = None
    priceComponent: Optional[List[InvoiceLineItemPriceComponent]] = empty_list()
    sequence: Optional[int] = None

    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", CodeableConcept, False, "chargeItem", True),
            ("chargeItemReference", "chargeItemReference", FHIRReference, False, "chargeItem", True),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("sequence", "sequence", int, False, None, False),
        ])
        return js


@dataclass
class Invoice(DomainResource):
    """ Invoice containing ChargeItems from an Account.

    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    resource_type: ClassVar[str] = "Invoice"
    account: Optional[FHIRReference] = None
    cancelledReason: Optional[str] = None
    date: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    issuer: Optional[FHIRReference] = None
    lineItem: Optional[List[InvoiceLineItem]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    participant: Optional[List[InvoiceParticipant]] = empty_list()
    paymentTerms: Optional[str] = None
    recipient: Optional[FHIRReference] = None
    status: str = None
    subject: Optional[FHIRReference] = None
    totalGross: Optional[Money] = None
    totalNet: Optional[Money] = None
    totalPriceComponent: Optional[List[InvoiceLineItemPriceComponent]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("account", "account", FHIRReference, False, None, False),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("issuer", "issuer", FHIRReference, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("recipient", "recipient", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", FHIRReference, False, None, False),
            ("totalGross", "totalGross", Money, False, None, False),
            ("totalNet", "totalNet", Money, False, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js