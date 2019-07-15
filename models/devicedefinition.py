#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceDefinition) on 2019-07-15.
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
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity

from . import domainresource

@dataclass
class DeviceDefinition(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    resource_type: ClassVar[str] = "DeviceDefinition"
    capability: Optional[List[DeviceDefinitionCapability]] = empty_list()
    contact: Optional[List[contactpoint.ContactPoint]] = empty_list()
    deviceName: Optional[List[DeviceDefinitionDeviceName]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    languageCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    manufacturerReference: Optional[fhirreference.FHIRReference] = None
    manufacturerString: Optional[str] = None
    material: Optional[List[DeviceDefinitionMaterial]] = empty_list()
    modelNumber: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    onlineInformation: Optional[str] = None
    owner: Optional[fhirreference.FHIRReference] = None
    parentDevice: Optional[fhirreference.FHIRReference] = None
    physicalCharacteristics: Optional[prodcharacteristic.ProdCharacteristic] = None
    property: Optional[List[DeviceDefinitionProperty]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    safety: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    shelfLifeStorage: Optional[List[productshelflife.ProductShelfLife]] = empty_list()
    specialization: Optional[List[DeviceDefinitionSpecialization]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    udiDeviceIdentifier: Optional[List[DeviceDefinitionUdiDeviceIdentifier]] = empty_list()
    url: Optional[str] = None
    version: Optional[List[str]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("capability", "capability", DeviceDefinitionCapability, True, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, True, None, False),
            ("manufacturerReference", "manufacturerReference", fhirreference.FHIRReference, False, "manufacturer", False),
            ("manufacturerString", "manufacturerString", str, False, "manufacturer", False),
            ("material", "material", DeviceDefinitionMaterial, True, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onlineInformation", "onlineInformation", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parentDevice", "parentDevice", fhirreference.FHIRReference, False, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("property", "property", DeviceDefinitionProperty, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("specialization", "specialization", DeviceDefinitionSpecialization, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """ Device capabilities.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionCapability"
    description: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("description", "description", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """ A name given to the device to identify it.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionDeviceName"
    name: str = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionMaterial"
    allergenicIndicator: Optional[bool] = None
    alternate: Optional[bool] = None
    substance:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("alternate", "alternate", bool, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js

@dataclass
class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionProperty"
    type:codeableconcept.CodeableConcept = None
    valueCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    valueQuantity: Optional[List[quantity.Quantity]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js

@dataclass
class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionSpecialization"
    systemType: str = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js

@dataclass
class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
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

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, False, None, True),
            ("issuer", "issuer", str, False, None, True),
            ("jurisdiction", "jurisdiction", str, False, None, True),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + '.prodcharacteristic']
try:
    from . import productshelflife
except ImportError:
    productshelflife = sys.modules[__package__ + '.productshelflife']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']