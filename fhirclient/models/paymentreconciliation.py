#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-07-18.
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
class PaymentReconciliationProcessNote(BackboneElement):
    """ Note concerning processing.

    A note that describes or explains the processing in a human readable form.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationProcessNote"
    text: Optional[str] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class PaymentReconciliationDetail(BackboneElement):
    """ Settlement particulars.

    Distribution of the payment amount for a previously acknowledged payable.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationDetail"
    amount: Optional[Money] = None
    date: Optional[FHIRDate] = None
    identifier: Optional[Identifier] = None
    payee: Optional[FHIRReference] = None
    predecessor: Optional[Identifier] = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    responsible: Optional[FHIRReference] = None
    submitter: Optional[FHIRReference] = None
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("payee", "payee", FHIRReference, False, None, False),
            ("predecessor", "predecessor", Identifier, False, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("response", "response", FHIRReference, False, None, False),
            ("responsible", "responsible", FHIRReference, False, None, False),
            ("submitter", "submitter", FHIRReference, False, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class PaymentReconciliation(DomainResource):
    """ PaymentReconciliation resource.

    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    resource_type: ClassVar[str] = "PaymentReconciliation"
    created: FHIRDate = None
    detail: Optional[List[PaymentReconciliationDetail]] = empty_list()
    disposition: Optional[str] = None
    formCode: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    outcome: Optional[str] = None
    paymentAmount: Money = None
    paymentDate: FHIRDate = None
    paymentIdentifier: Optional[Identifier] = None
    paymentIssuer: Optional[FHIRReference] = None
    period: Optional[Period] = None
    processNote: Optional[List[PaymentReconciliationProcessNote]] = empty_list()
    request: Optional[FHIRReference] = None
    requestor: Optional[FHIRReference] = None
    status: str = None

    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", FHIRDate, False, None, True),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("formCode", "formCode", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("paymentAmount", "paymentAmount", Money, False, None, True),
            ("paymentDate", "paymentDate", FHIRDate, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", Identifier, False, None, False),
            ("paymentIssuer", "paymentIssuer", FHIRReference, False, None, False),
            ("period", "period", Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", FHIRReference, False, None, False),
            ("requestor", "requestor", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js