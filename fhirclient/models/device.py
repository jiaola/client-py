#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Device) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactpoint import ContactPoint
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity


@dataclass
class DeviceVersion(BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    resource_type: ClassVar[str] = "DeviceVersion"
    component: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None
    value: str = None

    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


@dataclass
class DeviceUdiCarrier(BackboneElement):
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
class DeviceSpecialization(BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceSpecialization"
    systemType: CodeableConcept = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class DeviceProperty(BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceProperty"
    type: CodeableConcept = None
    valueCode: Optional[List[CodeableConcept]] = empty_list()
    valueQuantity: Optional[List[Quantity]] = empty_list()

    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("valueCode", "valueCode", CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", Quantity, True, None, False),
        ])
        return js


@dataclass
class DeviceDeviceName(BackboneElement):
    """ The name of the device as given by the manufacturer.

    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    resource_type: ClassVar[str] = "DeviceDeviceName"
    name: str = None
    type: str = None

    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class Device(DomainResource):
    """ Item used in healthcare.

    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    resource_type: ClassVar[str] = "Device"
    contact: Optional[List[ContactPoint]] = empty_list()
    definition: Optional[FHIRReference] = None
    deviceName: Optional[List[DeviceDeviceName]] = empty_list()
    distinctIdentifier: Optional[str] = None
    expirationDate: Optional[FHIRDate] = None
    identifier: Optional[List[Identifier]] = empty_list()
    location: Optional[FHIRReference] = None
    lotNumber: Optional[str] = None
    manufactureDate: Optional[FHIRDate] = None
    manufacturer: Optional[str] = None
    modelNumber: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    owner: Optional[FHIRReference] = None
    parent: Optional[FHIRReference] = None
    partNumber: Optional[str] = None
    patient: Optional[FHIRReference] = None
    property: Optional[List[DeviceProperty]] = empty_list()
    safety: Optional[List[CodeableConcept]] = empty_list()
    serialNumber: Optional[str] = None
    specialization: Optional[List[DeviceSpecialization]] = empty_list()
    status: Optional[str] = None
    statusReason: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[CodeableConcept] = None
    udiCarrier: Optional[List[DeviceUdiCarrier]] = empty_list()
    url: Optional[str] = None
    version: Optional[List[DeviceVersion]] = empty_list()

    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", ContactPoint, True, None, False),
            ("definition", "definition", FHIRReference, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("expirationDate", "expirationDate", FHIRDate, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("location", "location", FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufactureDate", "manufactureDate", FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("owner", "owner", FHIRReference, False, None, False),
            ("parent", "parent", FHIRReference, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("patient", "patient", FHIRReference, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("safety", "safety", CodeableConcept, True, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("status", "status", str, False, None, False),
            ("statusReason", "statusReason", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
        ])
        return js