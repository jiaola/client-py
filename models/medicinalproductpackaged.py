#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier
from . import marketingstatus
from . import prodcharacteristic
from . import productshelflife
from . import quantity

from . import domainresource

@dataclass
class MedicinalProductPackaged(domainresource.DomainResource):
    """ A medicinal product in a container or package.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackaged"
    batchIdentifier: Optional[List[MedicinalProductPackagedBatchIdentifier]] = empty_list()
    description: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    legalStatusOfSupply: Optional[codeableconcept.CodeableConcept] = None
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    marketingAuthorization: Optional[fhirreference.FHIRReference] = None
    marketingStatus: Optional[List[marketingstatus.MarketingStatus]] = empty_list()
    packageItem: List[ MedicinalProductPackagedPackageItem] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, True, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("marketingAuthorization", "marketingAuthorization", fhirreference.FHIRReference, False, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, True),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """ Batch numbering.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedBatchIdentifier"
    immediatePackaging: Optional[identifier.Identifier] = None
    outerPackaging:identifier.Identifier = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("immediatePackaging", "immediatePackaging", identifier.Identifier, False, None, False),
            ("outerPackaging", "outerPackaging", identifier.Identifier, False, None, True),
        ])
        return js

@dataclass
class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    resource_type: ClassVar[str] = "MedicinalProductPackagedPackageItem"
    alternateMaterial: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    device: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    manufacturedItem: Optional[List[fhirreference.FHIRReference]] = empty_list()
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    material: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    otherCharacteristics: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    packageItem: Optional[List[MedicinalProductPackagedPackageItem]] = empty_list()
    physicalCharacteristics: Optional[prodcharacteristic.ProdCharacteristic] = None
    quantity:quantity.Quantity = None
    shelfLifeStorage: Optional[List[productshelflife.ProductShelfLife]] = empty_list()
    type:codeableconcept.CodeableConcept = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, True, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manufacturedItem", "manufacturedItem", fhirreference.FHIRReference, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("material", "material", codeableconcept.CodeableConcept, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + '.marketingstatus']
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