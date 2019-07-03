#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Medication) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import ratio


from . import domainresource

@dataclass
class Medication(domainresource.DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    resource_type: ClassVar[str] = "Medication"
    amount: Optional[ratio.Ratio] = None
    batch: Optional[MedicationBatch] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    form: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    ingredient: Optional[List[MedicationIngredient]] = empty_list()
    manufacturer: Optional[fhirreference.FHIRReference] = None
    status: Optional[str] = None

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
#        self.amount = None
#        """ Amount of drug in package.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.batch = None
#        """ Details about packaged medications.
#        Type `MedicationBatch`
#
# (represented as `dict` in JSON). """
#
#
#        self.code = None
#        """ Codes that identify this medication.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.form = None
#        """ powder | tablets | capsule +.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Business identifier for this medication.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.ingredient = None
#        """ Active or inactive ingredient.
#        List of `MedicationIngredient` items
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturer = None
#        """ Manufacturer of the item.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ active | inactive | entered-in-error.
#        Type `str`
#
#. """
#

#        super(Medication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, {  # #}False, None, {  # #}False),
            ("batch", "batch", MedicationBatch, {  # #}False, None, {  # #}False),
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("form", "form", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("ingredient", "ingredient", MedicationIngredient, {  # #}True, None, {  # #}False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import ratio


from . import backboneelement

@dataclass
class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationBatch"
    expirationDate: Optional[fhirdate.FHIRDate] = None
    lotNumber: Optional[str] = None

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
#        self.expirationDate = None
#        """ When batch will expire.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.lotNumber = None
#        """ Identifier assigned to batch.
#        Type `str`
#
#. """
#

#        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("lotNumber", "lotNumber", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import ratio


@dataclass
class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationIngredient"
    isActive: Optional[bool] = None
    itemCodeableConcept:codeableconcept.CodeableConcept = None
    itemReference:fhirreference.FHIRReference = None
    strength: Optional[ratio.Ratio] = None

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
#        self.isActive = None
#        """ Active ingredient indicator.
#        Type `bool`
#
#. """
#
#
#        self.itemCodeableConcept = None
#        """ The actual ingredient or content.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.itemReference = None
#        """ The actual ingredient or content.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.strength = None
#        """ Quantity of ingredient present.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#

#        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, {  # #}False, None, {  # #}False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "item", {  # #}True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, {  # #}False, "item", {  # #}True),
            ("strength", "strength", ratio.Ratio, {  # #}False, None, {  # #}False),
        ])
        return js