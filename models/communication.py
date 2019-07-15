#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Communication) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import domainresource

@dataclass
class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.

    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """
    resource_type: ClassVar[str] = "Communication"
    about: Optional[List[fhirreference.FHIRReference]] = empty_list()
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    encounter: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    inResponseTo: Optional[List[fhirreference.FHIRReference]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    medium: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    partOf: Optional[List[fhirreference.FHIRReference]] = empty_list()
    payload: Optional[List[CommunicationPayload]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    received: Optional[fhirdate.FHIRDate] = None
    recipient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    sender: Optional[fhirreference.FHIRReference] = None
    sent: Optional[fhirdate.FHIRDate] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None
    subject: Optional[fhirreference.FHIRReference] = None
    topic: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("inResponseTo", "inResponseTo", fhirreference.FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("received", "received", fhirdate.FHIRDate, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("sent", "sent", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationPayload"
    contentAttachment:attachment.Attachment = None
    contentReference:fhirreference.FHIRReference = None
    contentString: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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