#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Medication) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .ratio import Ratio


@dataclass
class MedicationIngredient(BackboneElement):
    """ Active or inactive ingredient.

    Identifies a particular constituent of interest in the product.
    """
    resource_type: ClassVar[str] = "MedicationIngredient"
    isActive: Optional[bool] = None
    itemCodeableConcept: CodeableConcept = None
    itemReference: FHIRReference = None
    strength: Optional[Ratio] = None

    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", FHIRReference, False, "item", True),
            ("strength", "strength", Ratio, False, None, False),
        ])
        return js


@dataclass
class MedicationBatch(BackboneElement):
    """ Details about packaged medications.

    Information that only applies to packages (not products).
    """
    resource_type: ClassVar[str] = "MedicationBatch"
    expirationDate: Optional[FHIRDate] = None
    lotNumber: Optional[str] = None

    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", FHIRDate, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
        ])
        return js


@dataclass
class Medication(DomainResource):
    """ Definition of a Medication.

    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    resource_type: ClassVar[str] = "Medication"
    amount: Optional[Ratio] = None
    batch: Optional[MedicationBatch] = None
    code: Optional[CodeableConcept] = None
    form: Optional[CodeableConcept] = None
    identifier: Optional[List[Identifier]] = empty_list()
    ingredient: Optional[List[MedicationIngredient]] = empty_list()
    manufacturer: Optional[FHIRReference] = None
    status: Optional[str] = None

    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("amount", "amount", Ratio, False, None, False),
            ("batch", "batch", MedicationBatch, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("form", "form", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("ingredient", "ingredient", MedicationIngredient, True, None, False),
            ("manufacturer", "manufacturer", FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js