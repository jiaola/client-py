#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceDefinition) on 2019-07-18.
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
from .fhirreference import FHIRReference
from .identifier import Identifier
from .prodcharacteristic import ProdCharacteristic
from .productshelflife import ProductShelfLife
from .quantity import Quantity


@dataclass
class DeviceDefinitionUdiDeviceIdentifier(BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionUdiDeviceIdentifier"
    deviceIdentifier: str = None
    issuer: str = None
    jurisdiction: str = None

    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, False, None, True),
            ("issuer", "issuer", str, False, None, True),
            ("jurisdiction", "jurisdiction", str, False, None, True),
        ])
        return js


@dataclass
class DeviceDefinitionSpecialization(BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionSpecialization"
    systemType: str = None
    version: Optional[str] = None

    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


@dataclass
class DeviceDefinitionProperty(BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionProperty"
    type: CodeableConcept = None
    valueCode: Optional[List[CodeableConcept]] = empty_list()
    valueQuantity: Optional[List[Quantity]] = empty_list()

    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", CodeableConcept, False, None, True),
            ("valueCode", "valueCode", CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", Quantity, True, None, False),
        ])
        return js


@dataclass
class DeviceDefinitionMaterial(BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionMaterial"
    allergenicIndicator: Optional[bool] = None
    alternate: Optional[bool] = None
    substance: CodeableConcept = None

    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("alternate", "alternate", bool, False, None, False),
            ("substance", "substance", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class DeviceDefinitionDeviceName(BackboneElement):
    """ A name given to the device to identify it.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionDeviceName"
    name: str = None
    type: str = None

    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class DeviceDefinitionCapability(BackboneElement):
    """ Device capabilities.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionCapability"
    description: Optional[List[CodeableConcept]] = empty_list()
    type: CodeableConcept = None

    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("description", "description", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, True),
        ])
        return js


@dataclass
class DeviceDefinition(DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    resource_type: ClassVar[str] = "DeviceDefinition"
    capability: Optional[List[DeviceDefinitionCapability]] = empty_list()
    contact: Optional[List[ContactPoint]] = empty_list()
    deviceName: Optional[List[DeviceDefinitionDeviceName]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    languageCode: Optional[List[CodeableConcept]] = empty_list()
    manufacturerReference: Optional[FHIRReference] = None
    manufacturerString: Optional[str] = None
    material: Optional[List[DeviceDefinitionMaterial]] = empty_list()
    modelNumber: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    onlineInformation: Optional[str] = None
    owner: Optional[FHIRReference] = None
    parentDevice: Optional[FHIRReference] = None
    physicalCharacteristics: Optional[ProdCharacteristic] = None
    property: Optional[List[DeviceDefinitionProperty]] = empty_list()
    quantity: Optional[Quantity] = None
    safety: Optional[List[CodeableConcept]] = empty_list()
    shelfLifeStorage: Optional[List[ProductShelfLife]] = empty_list()
    specialization: Optional[List[DeviceDefinitionSpecialization]] = empty_list()
    type: Optional[CodeableConcept] = None
    udiDeviceIdentifier: Optional[List[DeviceDefinitionUdiDeviceIdentifier]] = empty_list()
    url: Optional[str] = None
    version: Optional[List[str]] = empty_list()

    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("capability", "capability", DeviceDefinitionCapability, True, None, False),
            ("contact", "contact", ContactPoint, True, None, False),
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("languageCode", "languageCode", CodeableConcept, True, None, False),
            ("manufacturerReference", "manufacturerReference", FHIRReference, False, "manufacturer", False),
            ("manufacturerString", "manufacturerString", str, False, "manufacturer", False),
            ("material", "material", DeviceDefinitionMaterial, True, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("onlineInformation", "onlineInformation", str, False, None, False),
            ("owner", "owner", FHIRReference, False, None, False),
            ("parentDevice", "parentDevice", FHIRReference, False, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", ProdCharacteristic, False, None, False),
            ("property", "property", DeviceDefinitionProperty, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("safety", "safety", CodeableConcept, True, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", ProductShelfLife, True, None, False),
            ("specialization", "specialization", DeviceDefinitionSpecialization, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, True, None, False),
        ])
        return js