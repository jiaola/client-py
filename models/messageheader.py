#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import fhirreference

from . import backboneelement

@dataclass
class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.

    The source application from which this message originated.
    """
    resource_type: ClassVar[str] = "MessageHeaderSource"
    contact: Optional[contactpoint.ContactPoint] = None
    endpoint: str = None
    name: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("software", "software", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

@dataclass
class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.

    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    resource_type: ClassVar[str] = "MessageHeaderResponse"
    code: str = None
    details: Optional[fhirreference.FHIRReference] = None
    identifier: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", str, False, None, True),
        ])
        return js

@dataclass
class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).

    The destination application which the message is intended for.
    """
    resource_type: ClassVar[str] = "MessageHeaderDestination"
    endpoint: str = None
    name: Optional[str] = None
    receiver: Optional[fhirreference.FHIRReference] = None
    target: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.

    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    resource_type: ClassVar[str] = "MessageHeader"
    author: Optional[fhirreference.FHIRReference] = None
    definition: Optional[str] = None
    destination: Optional[List[MessageHeaderDestination]] = empty_list()
    enterer: Optional[fhirreference.FHIRReference] = None
    eventCoding:coding.Coding = None
    eventUri: str = None
    focus: Optional[List[fhirreference.FHIRReference]] = empty_list()
    reason: Optional[codeableconcept.CodeableConcept] = None
    response: Optional[MessageHeaderResponse] = None
    responsible: Optional[fhirreference.FHIRReference] = None
    sender: Optional[fhirreference.FHIRReference] = None
    source: MessageHeaderSource = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']