#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import identifier
from . import usagecontext

from . import backboneelement

@dataclass
class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.

    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """
    resource_type: ClassVar[str] = "MessageDefinitionFocus"
    code: str = None
    max: Optional[str] = None
    min: int = None
    profile: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, True),
            ("profile", "profile", str, False, None, False),
        ])
        return js

@dataclass
class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.

    Indicates what types of messages may be sent as an application-level
    response to this message.
    """
    resource_type: ClassVar[str] = "MessageDefinitionAllowedResponse"
    message: str = None
    situation: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend([
            ("message", "message", str, False, None, True),
            ("situation", "situation", str, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.

    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """
    resource_type: ClassVar[str] = "MessageDefinition"
    allowedResponse: Optional[List[MessageDefinitionAllowedResponse]] = empty_list()
    base: Optional[str] = None
    category: Optional[str] = None
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date:fhirdate.FHIRDate = None
    description: Optional[str] = None
    eventCoding:coding.Coding = None
    eventUri: str = None
    experimental: Optional[bool] = None
    focus: Optional[List[MessageDefinitionFocus]] = empty_list()
    graph: Optional[List[str]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: Optional[str] = None
    parent: Optional[List[str]] = empty_list()
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    replaces: Optional[List[str]] = empty_list()
    responseRequired: Optional[str] = None
    status: str = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False),
            ("base", "base", str, False, None, False),
            ("category", "category", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("experimental", "experimental", bool, False, None, False),
            ("focus", "focus", MessageDefinitionFocus, True, None, False),
            ("graph", "graph", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("parent", "parent", str, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("responseRequired", "responseRequired", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']