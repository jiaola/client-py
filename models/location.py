#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Location) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier

from . import backboneelement

@dataclass
class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.

    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    resource_type: ClassVar[str] = "LocationPosition"
    altitude: Optional[float] = None
    latitude: float = None
    longitude: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("longitude", "longitude", float, False, None, True),
        ])
        return js

@dataclass
class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    resource_type: ClassVar[str] = "LocationHoursOfOperation"
    allDay: Optional[bool] = None
    closingTime: Optional[fhirdate.FHIRDate] = None
    daysOfWeek: Optional[List[str]] = empty_list()
    openingTime: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("closingTime", "closingTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("openingTime", "openingTime", fhirdate.FHIRDate, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.

    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    resource_type: ClassVar[str] = "Location"
    address: Optional[address.Address] = None
    alias: Optional[List[str]] = empty_list()
    availabilityExceptions: Optional[str] = None
    description: Optional[str] = None
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    hoursOfOperation: Optional[List[LocationHoursOfOperation]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    managingOrganization: Optional[fhirreference.FHIRReference] = None
    mode: Optional[str] = None
    name: Optional[str] = None
    operationalStatus: Optional[coding.Coding] = None
    partOf: Optional[fhirreference.FHIRReference] = None
    physicalType: Optional[codeableconcept.CodeableConcept] = None
    position: Optional[LocationPosition] = None
    status: Optional[str] = None
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("operationalStatus", "operationalStatus", coding.Coding, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("status", "status", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
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