#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import period

from . import domainresource

@dataclass
class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    resource_type: ClassVar[str] = "AuditEvent"
    action: Optional[str] = None
    agent: List[ AuditEventAgent] = empty_list()
    entity: Optional[List[AuditEventEntity]] = empty_list()
    outcome: Optional[str] = None
    outcomeDesc: Optional[str] = None
    period: Optional[period.Period] = None
    purposeOfEvent: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    recorded:fhirdate.FHIRDate = None
    source: AuditEventSource = None
    subtype: Optional[List[coding.Coding]] = empty_list()
    type:coding.Coding = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("entity", "entity", AuditEventEntity, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", codeableconcept.CodeableConcept, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js

from . import backboneelement

@dataclass
class AuditEventAgent(backboneelement.BackboneElement):
    """ Actor involved in the event.

    An actor taking an active role in the event or activity that is logged.
    """
    resource_type: ClassVar[str] = "AuditEventAgent"
    altId: Optional[str] = None
    location: Optional[fhirreference.FHIRReference] = None
    media: Optional[coding.Coding] = None
    name: Optional[str] = None
    network: Optional[AuditEventAgentNetwork] = None
    policy: Optional[List[str]] = empty_list()
    purposeOfUse: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    requestor: bool = None
    role: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    who: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("purposeOfUse", "purposeOfUse", codeableconcept.CodeableConcept, True, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """
    resource_type: ClassVar[str] = "AuditEventAgentNetwork"
    address: Optional[str] = None
    type: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js

@dataclass
class AuditEventEntity(backboneelement.BackboneElement):
    """ Data or objects used.

    Specific instances of data or objects that have been accessed.
    """
    resource_type: ClassVar[str] = "AuditEventEntity"
    description: Optional[str] = None
    detail: Optional[List[AuditEventEntityDetail]] = empty_list()
    lifecycle: Optional[coding.Coding] = None
    name: Optional[str] = None
    query: Optional[str] = None
    role: Optional[coding.Coding] = None
    securityLabel: Optional[List[coding.Coding]] = empty_list()
    type: Optional[coding.Coding] = None
    what: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("what", "what", fhirreference.FHIRReference, False, None, False),
        ])
        return js

@dataclass
class AuditEventEntityDetail(backboneelement.BackboneElement):
    """ Additional Information about the entity.

    Tagged value pairs for conveying additional information about the entity.
    """
    resource_type: ClassVar[str] = "AuditEventEntityDetail"
    type: str = None
    valueBase64Binary: str = None
    valueString: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js

@dataclass
class AuditEventSource(backboneelement.BackboneElement):
    """ Audit Event Reporter.

    The system that is reporting the event.
    """
    resource_type: ClassVar[str] = "AuditEventSource"
    observer:fhirreference.FHIRReference = None
    site: Optional[str] = None
    type: Optional[List[coding.Coding]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("observer", "observer", fhirreference.FHIRReference, False, None, True),
            ("site", "site", str, False, None, False),
            ("type", "type", coding.Coding, True, None, False),
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
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']