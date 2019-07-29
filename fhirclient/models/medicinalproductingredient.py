#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient) on 2019-07-29.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier
from .ratio import Ratio


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    substance: Optional[CodeableConcept] = None
    strength: Ratio = None
    strengthLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("substance", "substance", CodeableConcept, False, None, False),
            ("strength", "strength", Ratio, False, None, True),
            ("strengthLowLimit", "strengthLowLimit", Ratio, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrength(BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrength"
    presentation: Ratio = None
    presentationLowLimit: Optional[Ratio] = None
    concentration: Optional[Ratio] = None
    concentrationLowLimit: Optional[Ratio] = None
    measurementPoint: Optional[str] = None
    country: Optional[List[CodeableConcept]] = empty_list()
    referenceStrength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("presentation", "presentation", Ratio, False, None, True),
            ("presentationLowLimit", "presentationLowLimit", Ratio, False, None, False),
            ("concentration", "concentration", Ratio, False, None, False),
            ("concentrationLowLimit", "concentrationLowLimit", Ratio, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", CodeableConcept, True, None, False),
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductIngredientSpecifiedSubstance(BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstance"
    code: CodeableConcept = None
    group: CodeableConcept = None
    confidentiality: Optional[CodeableConcept] = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("group", "group", CodeableConcept, False, None, True),
            ("confidentiality", "confidentiality", CodeableConcept, False, None, False),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductIngredientSubstance(BackboneElement):
    """ The ingredient substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSubstance"
    code: CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js


@dataclass
class MedicinalProductIngredient(DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredient"
    identifier: Optional[Identifier] = None
    role: CodeableConcept = None
    allergenicIndicator: Optional[bool] = None
    manufacturer: Optional[List[FHIRReference]] = empty_list()
    specifiedSubstance: Optional[List[MedicinalProductIngredientSpecifiedSubstance]] = empty_list()
    substance: Optional[MedicinalProductIngredientSubstance] = None

    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, False, None, False),
            ("role", "role", CodeableConcept, False, None, True),
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("manufacturer", "manufacturer", FHIRReference, True, None, False),
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, True, None, False),
            ("substance", "substance", MedicinalProductIngredientSubstance, False, None, False),
        ])
        return js