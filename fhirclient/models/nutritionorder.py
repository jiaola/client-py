#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio
from .timing import Timing


@dataclass
class NutritionOrderSupplement(BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderSupplement"
    instruction: Optional[str] = None
    productName: Optional[str] = None
    quantity: Optional[Quantity] = None
    schedule: Optional[List[Timing]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("schedule", "schedule", Timing, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderOralDietTexture(BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietTexture"
    foodType: Optional[CodeableConcept] = None
    modifier: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", CodeableConcept, False, None, False),
            ("modifier", "modifier", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderOralDietNutrient(BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietNutrient"
    amount: Optional[Quantity] = None
    modifier: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", Quantity, False, None, False),
            ("modifier", "modifier", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderOralDiet(BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDiet"
    fluidConsistencyType: Optional[List[CodeableConcept]] = empty_list()
    instruction: Optional[str] = None
    nutrient: Optional[List[NutritionOrderOralDietNutrient]] = empty_list()
    schedule: Optional[List[Timing]] = empty_list()
    texture: Optional[List[NutritionOrderOralDietTexture]] = empty_list()
    type: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", CodeableConcept, True, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True, None, False),
            ("schedule", "schedule", Timing, True, None, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True, None, False),
            ("type", "type", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class NutritionOrderEnteralFormulaAdministration(BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormulaAdministration"
    quantity: Optional[Quantity] = None
    rateQuantity: Optional[Quantity] = None
    rateRatio: Optional[Ratio] = None
    schedule: Optional[Timing] = None

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("quantity", "quantity", Quantity, False, None, False),
            ("rateQuantity", "rateQuantity", Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", Ratio, False, "rate", False),
            ("schedule", "schedule", Timing, False, None, False),
        ])
        return js


@dataclass
class NutritionOrderEnteralFormula(BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormula"
    additiveProductName: Optional[str] = None
    additiveType: Optional[CodeableConcept] = None
    administration: Optional[List[NutritionOrderEnteralFormulaAdministration]] = empty_list()
    administrationInstruction: Optional[str] = None
    baseFormulaProductName: Optional[str] = None
    baseFormulaType: Optional[CodeableConcept] = None
    caloricDensity: Optional[Quantity] = None
    maxVolumeToDeliver: Optional[Quantity] = None
    routeofAdministration: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("additiveType", "additiveType", CodeableConcept, False, None, False),
            ("administration", "administration", NutritionOrderEnteralFormulaAdministration, True, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("baseFormulaType", "baseFormulaType", CodeableConcept, False, None, False),
            ("caloricDensity", "caloricDensity", Quantity, False, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", Quantity, False, None, False),
            ("routeofAdministration", "routeofAdministration", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class NutritionOrder(DomainResource):
    """ Diet, formula or nutritional supplement request.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    resource_type: ClassVar[str] = "NutritionOrder"
    allergyIntolerance: Optional[List[FHIRReference]] = empty_list()
    dateTime: FHIRDate = None
    encounter: Optional[FHIRReference] = None
    enteralFormula: Optional[NutritionOrderEnteralFormula] = None
    excludeFoodModifier: Optional[List[CodeableConcept]] = empty_list()
    foodPreferenceModifier: Optional[List[CodeableConcept]] = empty_list()
    identifier: Optional[List[Identifier]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[Annotation]] = empty_list()
    oralDiet: Optional[NutritionOrderOralDiet] = None
    orderer: Optional[FHIRReference] = None
    patient: FHIRReference = None
    status: str = None
    supplement: Optional[List[NutritionOrderSupplement]] = empty_list()

    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", FHIRReference, True, None, False),
            ("dateTime", "dateTime", FHIRDate, False, None, True),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", CodeableConcept, True, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", CodeableConcept, True, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", Annotation, True, None, False),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False, None, False),
            ("orderer", "orderer", FHIRReference, False, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
            ("supplement", "supplement", NutritionOrderSupplement, True, None, False),
        ])
        return js