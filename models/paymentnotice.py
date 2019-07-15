#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money

from . import domainresource

@dataclass
class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    resource_type: ClassVar[str] = "PaymentNotice"
    amount:money.Money = None
    created:fhirdate.FHIRDate = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    payee: Optional[fhirreference.FHIRReference] = None
    payment:fhirreference.FHIRReference = None
    paymentDate: Optional[fhirdate.FHIRDate] = None
    paymentStatus: Optional[codeableconcept.CodeableConcept] = None
    provider: Optional[fhirreference.FHIRReference] = None
    recipient:fhirreference.FHIRReference = None
    request: Optional[fhirreference.FHIRReference] = None
    response: Optional[fhirreference.FHIRReference] = None
    status: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("payment", "payment", fhirreference.FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
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