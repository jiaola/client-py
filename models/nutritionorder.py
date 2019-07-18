#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
from . import timing

from . import backboneelement

@dataclass
class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ Supplement components.

    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderSupplement"
    instruction: Optional[str] = None
    productName: Optional[str] = None
    quantity: Optional[quantity.Quantity] = None
    schedule: Optional[List[timing.Timing]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.

    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietTexture"
    foodType: Optional[codeableconcept.CodeableConcept] = None
    modifier: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", codeableconcept.CodeableConcept, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.

    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDietNutrient"
    amount: Optional[quantity.Quantity] = None
    modifier: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.

    Diet given orally in contrast to enteral (tube) feeding.
    """
    resource_type: ClassVar[str] = "NutritionOrderOralDiet"
    fluidConsistencyType: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    instruction: Optional[str] = None
    nutrient: Optional[List[NutritionOrderOralDietNutrient]] = empty_list()
    schedule: Optional[List[timing.Timing]] = empty_list()
    texture: Optional[List[NutritionOrderOralDietTexture]] = empty_list()
    type: Optional[List[codeableconcept.CodeableConcept]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", codeableconcept.CodeableConcept, True, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js

@dataclass
class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.

    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormulaAdministration"
    quantity: Optional[quantity.Quantity] = None
    rateQuantity: Optional[quantity.Quantity] = None
    rateRatio: Optional[ratio.Ratio] = None
    schedule: Optional[timing.Timing] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("schedule", "schedule", timing.Timing, False, None, False),
        ])
        return js

@dataclass
class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.

    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    resource_type: ClassVar[str] = "NutritionOrderEnteralFormula"
    additiveProductName: Optional[str] = None
    additiveType: Optional[codeableconcept.CodeableConcept] = None
    administration: Optional[List[NutritionOrderEnteralFormulaAdministration]] = empty_list()
    administrationInstruction: Optional[str] = None
    baseFormulaProductName: Optional[str] = None
    baseFormulaType: Optional[codeableconcept.CodeableConcept] = None
    caloricDensity: Optional[quantity.Quantity] = None
    maxVolumeToDeliver: Optional[quantity.Quantity] = None
    routeofAdministration: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("additiveType", "additiveType", codeableconcept.CodeableConcept, False, None, False),
            ("administration", "administration", NutritionOrderEnteralFormulaAdministration, True, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("baseFormulaType", "baseFormulaType", codeableconcept.CodeableConcept, False, None, False),
            ("caloricDensity", "caloricDensity", quantity.Quantity, False, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", quantity.Quantity, False, None, False),
            ("routeofAdministration", "routeofAdministration", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class NutritionOrder(domainresource.DomainResource):
    """ Diet, formula or nutritional supplement request.

    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    resource_type: ClassVar[str] = "NutritionOrder"
    allergyIntolerance: Optional[List[fhirreference.FHIRReference]] = empty_list()
    dateTime:fhirdate.FHIRDate = None
    encounter: Optional[fhirreference.FHIRReference] = None
    enteralFormula: Optional[NutritionOrderEnteralFormula] = None
    excludeFoodModifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    foodPreferenceModifier: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    instantiates: Optional[List[str]] = empty_list()
    instantiatesCanonical: Optional[List[str]] = empty_list()
    instantiatesUri: Optional[List[str]] = empty_list()
    intent: str = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    oralDiet: Optional[NutritionOrderOralDiet] = None
    orderer: Optional[fhirreference.FHIRReference] = None
    patient:fhirreference.FHIRReference = None
    status: str = None
    supplement: Optional[List[NutritionOrderSupplement]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", fhirreference.FHIRReference, True, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", codeableconcept.CodeableConcept, True, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False, None, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
            ("supplement", "supplement", NutritionOrderSupplement, True, None, False),
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
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']