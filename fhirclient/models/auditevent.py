#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .coding import Coding
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class AuditEventSource(BackboneElement):
    """ Audit Event Reporter.

    The system that is reporting the event.
    """
    resource_type: ClassVar[str] = "AuditEventSource"
    observer: FHIRReference = None
    site: Optional[str] = None
    type: Optional[List[Coding]] = empty_list()

    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("observer", "observer", FHIRReference, False, None, True),
            ("site", "site", str, False, None, False),
            ("type", "type", Coding, True, None, False),
        ])
        return js


@dataclass
class AuditEventEntityDetail(BackboneElement):
    """ Additional Information about the entity.

    Tagged value pairs for conveying additional information about the entity.
    """
    resource_type: ClassVar[str] = "AuditEventEntityDetail"
    type: str = None
    valueBase64Binary: str = None
    valueString: str = None

    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


@dataclass
class AuditEventEntity(BackboneElement):
    """ Data or objects used.

    Specific instances of data or objects that have been accessed.
    """
    resource_type: ClassVar[str] = "AuditEventEntity"
    description: Optional[str] = None
    detail: Optional[List[AuditEventEntityDetail]] = empty_list()
    lifecycle: Optional[Coding] = None
    name: Optional[str] = None
    query: Optional[str] = None
    role: Optional[Coding] = None
    securityLabel: Optional[List[Coding]] = empty_list()
    type: Optional[Coding] = None
    what: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
            ("lifecycle", "lifecycle", Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("role", "role", Coding, False, None, False),
            ("securityLabel", "securityLabel", Coding, True, None, False),
            ("type", "type", Coding, False, None, False),
            ("what", "what", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class AuditEventAgentNetwork(BackboneElement):
    """ Logical network location for application activity.

    Logical network location for application activity, if the activity has a
    network location.
    """
    resource_type: ClassVar[str] = "AuditEventAgentNetwork"
    address: Optional[str] = None
    type: Optional[str] = None

    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


@dataclass
class AuditEventAgent(BackboneElement):
    """ Actor involved in the event.

    An actor taking an active role in the event or activity that is logged.
    """
    resource_type: ClassVar[str] = "AuditEventAgent"
    altId: Optional[str] = None
    location: Optional[FHIRReference] = None
    media: Optional[Coding] = None
    name: Optional[str] = None
    network: Optional[AuditEventAgentNetwork] = None
    policy: Optional[List[str]] = empty_list()
    purposeOfUse: Optional[List[CodeableConcept]] = empty_list()
    requestor: bool = None
    role: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[CodeableConcept] = None
    who: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("media", "media", Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("purposeOfUse", "purposeOfUse", CodeableConcept, True, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("role", "role", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("who", "who", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class AuditEvent(DomainResource):
    """ Event record kept for security purposes.

    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    resource_type: ClassVar[str] = "AuditEvent"
    action: Optional[str] = None
    agent: List[AuditEventAgent] = empty_list()
    entity: Optional[List[AuditEventEntity]] = empty_list()
    outcome: Optional[str] = None
    outcomeDesc: Optional[str] = None
    period: Optional[Period] = None
    purposeOfEvent: Optional[List[CodeableConcept]] = empty_list()
    recorded: FHIRDate = None
    source: AuditEventSource = None
    subtype: Optional[List[Coding]] = empty_list()
    type: Coding = None

    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("entity", "entity", AuditEventEntity, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("period", "period", Period, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", CodeableConcept, True, None, False),
            ("recorded", "recorded", FHIRDate, False, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("subtype", "subtype", Coding, True, None, False),
            ("type", "type", Coding, False, None, True),
        ])
        return js