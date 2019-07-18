#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Device) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity

from . import backboneelement

@dataclass
class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    resource_type: ClassVar[str] = "DeviceVersion"
    component: Optional[identifier.Identifier] = None
    type: Optional[codeableconcept.CodeableConcept] = None
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js

@dataclass
class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    resource_type: ClassVar[str] = "DeviceUdiCarrier"
    carrierAIDC: Optional[str] = None
    carrierHRF: Optional[str] = None
    deviceIdentifier: Optional[str] = None
    entryType: Optional[str] = None
    issuer: Optional[str] = None
    jurisdiction: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
        ])
        return js

@dataclass
class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceSpecialization"
    systemType:codeableconcept.CodeableConcept = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js

@dataclass
class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceProperty"
    type:codeableconcept.CodeableConcept = None
    valueCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    valueQuantity: Optional[List[quantity.Quantity]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js

@dataclass
class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.

    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    resource_type: ClassVar[str] = "DeviceDeviceName"
    name: str = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js

from . import domainresource

@dataclass
class Device(domainresource.DomainResource):
    """ Item used in healthcare.

    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    resource_type: ClassVar[str] = "Device"
    contact: Optional[List[contactpoint.ContactPoint]] = empty_list()
    definition: Optional[fhirreference.FHIRReference] = None
    deviceName: Optional[List[DeviceDeviceName]] = empty_list()
    distinctIdentifier: Optional[str] = None
    expirationDate: Optional[fhirdate.FHIRDate] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    lotNumber: Optional[str] = None
    manufactureDate: Optional[fhirdate.FHIRDate] = None
    manufacturer: Optional[str] = None
    modelNumber: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    owner: Optional[fhirreference.FHIRReference] = None
    parent: Optional[fhirreference.FHIRReference] = None
    partNumber: Optional[str] = None
    patient: Optional[fhirreference.FHIRReference] = None
    property: Optional[List[DeviceProperty]] = empty_list()
    safety: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    serialNumber: Optional[str] = None
    specialization: Optional[List[DeviceSpecialization]] = empty_list()
    status: Optional[str] = None
    statusReason: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    udiCarrier: Optional[List[DeviceUdiCarrier]] = empty_list()
    url: Optional[str] = None
    version: Optional[List[DeviceVersion]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("status", "status", str, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']