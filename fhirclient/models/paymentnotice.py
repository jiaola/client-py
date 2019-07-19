#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money


@dataclass
class PaymentNotice(DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    resource_type: ClassVar[str] = "PaymentNotice"
    amount: Money = None
    created: FHIRDate = None
    identifier: Optional[List[Identifier]] = empty_list()
    payee: Optional[FHIRReference] = None
    payment: FHIRReference = None
    paymentDate: Optional[FHIRDate] = None
    paymentStatus: Optional[CodeableConcept] = None
    provider: Optional[FHIRReference] = None
    recipient: FHIRReference = None
    request: Optional[FHIRReference] = None
    response: Optional[FHIRReference] = None
    status: str = None

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("amount", "amount", Money, False, None, True),
            ("created", "created", FHIRDate, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("payee", "payee", FHIRReference, False, None, False),
            ("payment", "payment", FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", FHIRDate, False, None, False),
            ("paymentStatus", "paymentStatus", CodeableConcept, False, None, False),
            ("provider", "provider", FHIRReference, False, None, False),
            ("recipient", "recipient", FHIRReference, False, None, True),
            ("request", "request", FHIRReference, False, None, False),
            ("response", "response", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js