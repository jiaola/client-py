#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period

from . import backboneelement

@dataclass
class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Note concerning processing.

    A note that describes or explains the processing in a human readable form.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationProcessNote"
    text: Optional[str] = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Settlement particulars.

    Distribution of the payment amount for a previously acknowledged payable.
    """
    resource_type: ClassVar[str] = "PaymentReconciliationDetail"
    amount: Optional[money.Money] = None
    date: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[identifier.Identifier] = None
    payee: Optional[fhirreference.FHIRReference] = None
    predecessor: Optional[identifier.Identifier] = None
    request: Optional[fhirreference.FHIRReference] = None
    response: Optional[fhirreference.FHIRReference] = None
    responsible: Optional[fhirreference.FHIRReference] = None
    submitter: Optional[fhirreference.FHIRReference] = None
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("predecessor", "predecessor", identifier.Identifier, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.

    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    resource_type: ClassVar[str] = "PaymentReconciliation"
    created:fhirdate.FHIRDate = None
    detail: Optional[List[PaymentReconciliationDetail]] = empty_list()
    disposition: Optional[str] = None
    formCode: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    outcome: Optional[str] = None
    paymentAmount:money.Money = None
    paymentDate:fhirdate.FHIRDate = None
    paymentIdentifier: Optional[identifier.Identifier] = None
    paymentIssuer: Optional[fhirreference.FHIRReference] = None
    period: Optional[period.Period] = None
    processNote: Optional[List[PaymentReconciliationProcessNote]] = empty_list()
    request: Optional[fhirreference.FHIRReference] = None
    requestor: Optional[fhirreference.FHIRReference] = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("paymentAmount", "paymentAmount", money.Money, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False),
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


import sys
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