#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged) on 2019-07-03.
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
#        self.batchIdentifier = None
#        """ Batch numbering.
#        List of `MedicinalProductPackagedBatchIdentifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Textual description.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ Unique identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.legalStatusOfSupply = None
#        """ The legal status of supply of the medicinal product as classified
        by the regulator.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturer = None
#        """ Manufacturer of this Package Item.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.marketingAuthorization = None
#        """ Manufacturer of this Package Item.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.marketingStatus = None
#        """ Marketing information.
#        List of `MarketingStatus` items
#
# (represented as `dict` in JSON). """
#
#
#        self.packageItem = None
#        """ A packaging item, as a contained for medicine, possibly with other
        packaging items within.
#        List of `MedicinalProductPackagedPackageItem` items
#
# (represented as `dict` in JSON). """
#
#
#        self.subject = None
#        """ The product with this is a pack for.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductPackaged, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, {  # #}True, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("marketingAuthorization", "marketingAuthorization", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, {  # #}True, None, {  # #}False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, {  # #}True, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirreference
from . import identifier
from . import marketingstatus
from . import prodcharacteristic
from . import productshelflife
from . import quantity


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
#        self.immediatePackaging = None
#        """ A number appearing on the immediate packaging (and not the outer
        packaging).
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.outerPackaging = None
#        """ A number appearing on the outer packaging of a specific batch.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductPackagedBatchIdentifier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("immediatePackaging", "immediatePackaging", identifier.Identifier, {  # #}False, None, {  # #}False),
            ("outerPackaging", "outerPackaging", identifier.Identifier, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import marketingstatus
from . import prodcharacteristic
from . import productshelflife
from . import quantity


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
#        self.alternateMaterial = None
#        """ A possible alternate material for the packaging.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.device = None
#        """ A device accompanying a medicinal product.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Including possibly Data Carrier Identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturedItem = None
#        """ The manufactured item as contained in the packaged medicinal
        product.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturer = None
#        """ Manufacturer of this Package Item.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.material = None
#        """ Material type of the package item.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.otherCharacteristics = None
#        """ Other codeable characteristics.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.packageItem = None
#        """ Allows containers within containers.
#        List of `MedicinalProductPackagedPackageItem` items
#
# (represented as `dict` in JSON). """
#
#
#        self.physicalCharacteristics = None
#        """ Dimensions, color etc..
#        Type `ProdCharacteristic`
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ The quantity of this package in the medicinal product, at the
        current level of packaging. The outermost is always 1.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.shelfLifeStorage = None
#        """ Shelf Life and storage information.
#        List of `ProductShelfLife` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ The physical type of the container of the medicine.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductPackagedPackageItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("device", "device", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("manufacturedItem", "manufacturedItem", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("material", "material", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, {  # #}True, None, {  # #}False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, {  # #}False, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}True),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js