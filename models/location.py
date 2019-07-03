#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Location) on 2019-07-03.
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
#        self.address = None
#        """ Physical location.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.alias = None
#        """ A list of alternate names that the location is known as, or was
        known as, in the past.
#        List of `str` items
#
#. """
#
#
#        self.availabilityExceptions = None
#        """ Description of availability exceptions.
#        Type `str`
#
#. """
#
#
#        self.description = None
#        """ Additional details about the location that could be displayed as
        further information to identify the location beyond its name.
#        Type `str`
#
#. """
#
#
#        self.endpoint = None
#        """ Technical endpoints providing access to services operated for the
        location.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.hoursOfOperation = None
#        """ What days/times during a week is this location usually open.
#        List of `LocationHoursOfOperation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Unique code or number identifying the location to its users.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.managingOrganization = None
#        """ Organization responsible for provisioning and upkeep.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.mode = None
#        """ instance | kind.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name of the location as used by humans.
#        Type `str`
#
#. """
#
#
#        self.operationalStatus = None
#        """ The operational status of the location (typically only for a
        bed/room).
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.partOf = None
#        """ Another Location this one is physically a part of.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.physicalType = None
#        """ Physical form of the location.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.position = None
#        """ The absolute geographic location.
#        Type `LocationPosition`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | suspended | inactive.
#        Type `str`
#
#. """
#
#
#        self.telecom = None
#        """ Contact details of the location.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Type of function performed.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#

#        super(Location, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, {  # #}False, None, {  # #}False),
            ("alias", "alias", str, {  # #}True, None, {  # #}False),
            ("availabilityExceptions", "availabilityExceptions", str, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("operationalStatus", "operationalStatus", coding.Coding, {  # #}False, None, {  # #}False),
            ("partOf", "partOf", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("position", "position", LocationPosition, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier


from . import backboneelement

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
#        self.allDay = None
#        """ The Location is open all day.
#        Type `bool`
#
#. """
#
#
#        self.closingTime = None
#        """ Time that the Location closes.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.daysOfWeek = None
#        """ mon | tue | wed | thu | fri | sat | sun.
#        List of `str` items
#
#. """
#
#
#        self.openingTime = None
#        """ Time that the Location opens.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#

#        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, {  # #}False, None, {  # #}False),
            ("closingTime", "closingTime", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("daysOfWeek", "daysOfWeek", str, {  # #}True, None, {  # #}False),
            ("openingTime", "openingTime", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier


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
#        self.altitude = None
#        """ Altitude with WGS84 datum.
#        Type `float`
#
#. """
#
#
#        self.latitude = None
#        """ Latitude with WGS84 datum.
#        Type `float`
#
#. """
#
#
#        self.longitude = None
#        """ Longitude with WGS84 datum.
#        Type `float`
#
#. """
#

#        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, {  # #}False, None, {  # #}False),
            ("latitude", "latitude", float, {  # #}False, None, {  # #}True),
            ("longitude", "longitude", float, {  # #}False, None, {  # #}True),
        ])
        return js