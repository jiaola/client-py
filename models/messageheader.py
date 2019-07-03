#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2019-07-03.
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
#        self.author = None
#        """ The source of the decision.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.definition = None
#        """ Link to the definition for this message.
#        Type `str`
#
#. """
#
#
#        self.destination = None
#        """ Message destination application(s).
#        List of `MessageHeaderDestination` items
#
# (represented as `dict` in JSON). """
#
#
#        self.enterer = None
#        """ The source of the data entry.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.eventCoding = None
#        """ Code for the event this message represents or link to event
        definition.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.eventUri = None
#        """ Code for the event this message represents or link to event
        definition.
#        Type `str`
#
#. """
#
#
#        self.focus = None
#        """ The actual content of the message.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reason = None
#        """ Cause of event.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.response = None
#        """ If this is a reply to prior message.
#        Type `MessageHeaderResponse`
#
# (represented as `dict` in JSON). """
#
#
#        self.responsible = None
#        """ Final responsibility for event.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.sender = None
#        """ Real world sender of the message.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Message source application.
#        Type `MessageHeaderSource`
#
# (represented as `dict` in JSON). """
#

#        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("definition", "definition", str, {  # #}False, None, {  # #}False),
            ("destination", "destination", MessageHeaderDestination, {  # #}True, None, {  # #}False),
            ("enterer", "enterer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("eventCoding", "eventCoding", coding.Coding, {  # #}False, "event", {  # #}True),
            ("eventUri", "eventUri", str, {  # #}False, "event", {  # #}True),
            ("focus", "focus", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("reason", "reason", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("response", "response", MessageHeaderResponse, {  # #}False, None, {  # #}False),
            ("responsible", "responsible", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("sender", "sender", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("source", "source", MessageHeaderSource, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference


from . import backboneelement

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
#        self.endpoint = None
#        """ Actual destination address or id.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name of system.
#        Type `str`
#
#. """
#
#
#        self.receiver = None
#        """ Intended "real-world" recipient for the data.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.target = None
#        """ Particular delivery destination within the destination.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, {  # #}False, None, {  # #}True),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("receiver", "receiver", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("target", "target", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference


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
#        self.code = None
#        """ ok | transient-error | fatal-error.
#        Type `str`
#
#. """
#
#
#        self.details = None
#        """ Specific list of hints/warnings/errors.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Id of original message.
#        Type `str`
#
#. """
#

#        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, {  # #}False, None, {  # #}True),
            ("details", "details", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference


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
#        self.contact = None
#        """ Human contact for problems.
#        Type `ContactPoint`
#
# (represented as `dict` in JSON). """
#
#
#        self.endpoint = None
#        """ Actual message source address or id.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name of system.
#        Type `str`
#
#. """
#
#
#        self.software = None
#        """ Name of software running the system.
#        Type `str`
#
#. """
#
#
#        self.version = None
#        """ Version of software running.
#        Type `str`
#
#. """
#

#        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, {  # #}False, None, {  # #}False),
            ("endpoint", "endpoint", str, {  # #}False, None, {  # #}True),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("software", "software", str, {  # #}False, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js