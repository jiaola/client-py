#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Subscription) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate


@dataclass
class SubscriptionChannel(BackboneElement):
    """ The channel on which to report matches to the criteria.

    Details where to send notifications when resources are received that meet
    the criteria.
    """
    resource_type: ClassVar[str] = "SubscriptionChannel"
    endpoint: Optional[str] = None
    header: Optional[List[str]] = empty_list()
    payload: Optional[str] = None
    type: str = None

    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, False),
            ("header", "header", str, True, None, False),
            ("payload", "payload", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class Subscription(DomainResource):
    """ Server push subscription criteria.

    The subscription resource is used to define a push-based subscription from
    a server to another system. Once a subscription is registered with the
    server, the server checks every resource that is created or updated, and if
    the resource matches the given criteria, it sends a message on the defined
    "channel" so that another system can take an appropriate action.
    """
    resource_type: ClassVar[str] = "Subscription"
    channel: SubscriptionChannel = None
    contact: Optional[List[ContactPoint]] = empty_list()
    criteria: str = None
    end: Optional[FHIRDate] = None
    error: Optional[str] = None
    reason: str = None
    status: str = None

    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("channel", "channel", SubscriptionChannel, False, None, True),
            ("contact", "contact", ContactPoint, True, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("end", "end", FHIRDate, False, None, False),
            ("error", "error", str, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js