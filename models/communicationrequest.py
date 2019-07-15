#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2019-07-15.
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
from . import period

from . import domainresource

@dataclass
class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    resource_type: ClassVar[str] = "CommunicationRequest"
    about: Optional[List[fhirreference.FHIRReference]] = empty_list()
    authoredOn: Optional[fhirdate.FHIRDate] = None
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    category: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    doNotPerform: Optional[bool] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    groupIdentifier: Optional[identifier.Identifier] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    medium: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    occurrenceDateTime: Optional[fhirdate.FHIRDate] = None
    occurrencePeriod: Optional[period.Period] = None
    payload: Optional[List[CommunicationRequestPayload]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    recipient: Optional[List[fhirreference.FHIRReference]] = empty_list()
    replaces: Optional[List[fhirreference.FHIRReference]] = empty_list()
    requester: Optional[fhirreference.FHIRReference] = None
    sender: Optional[fhirreference.FHIRReference] = None
    status: str = None
    statusReason: Optional[codeableconcept.CodeableConcept] = None
    subject: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationRequestPayload"
    contentAttachment:attachment.Attachment = None
    contentReference:fhirreference.FHIRReference = None
    contentString: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']