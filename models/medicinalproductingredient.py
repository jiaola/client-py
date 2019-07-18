#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient) on 2019-07-18.
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
from . import ratio

from . import backboneelement

@dataclass
class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ The ingredient substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSubstance"
    code:codeableconcept.CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js

@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    country: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    measurementPoint: Optional[str] = None
    strength:ratio.Ratio = None
    strengthLowLimit: Optional[ratio.Ratio] = None
    substance: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("strength", "strength", ratio.Ratio, False, None, True),
            ("strengthLowLimit", "strengthLowLimit", ratio.Ratio, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MedicinalProductIngredientSpecifiedSubstanceStrength(backboneelement.BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstanceStrength"
    concentration: Optional[ratio.Ratio] = None
    concentrationLowLimit: Optional[ratio.Ratio] = None
    country: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    measurementPoint: Optional[str] = None
    presentation:ratio.Ratio = None
    presentationLowLimit: Optional[ratio.Ratio] = None
    referenceStrength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("concentration", "concentration", ratio.Ratio, False, None, False),
            ("concentrationLowLimit", "concentrationLowLimit", ratio.Ratio, False, None, False),
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("presentation", "presentation", ratio.Ratio, False, None, True),
            ("presentationLowLimit", "presentationLowLimit", ratio.Ratio, False, None, False),
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False),
        ])
        return js

@dataclass
class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredientSpecifiedSubstance"
    code:codeableconcept.CodeableConcept = None
    confidentiality: Optional[codeableconcept.CodeableConcept] = None
    group:codeableconcept.CodeableConcept = None
    strength: Optional[List[MedicinalProductIngredientSpecifiedSubstanceStrength]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, False, None, False),
            ("group", "group", codeableconcept.CodeableConcept, False, None, True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class MedicinalProductIngredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIngredient"
    allergenicIndicator: Optional[bool] = None
    identifier: Optional[identifier.Identifier] = None
    manufacturer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    role:codeableconcept.CodeableConcept = None
    specifiedSubstance: Optional[List[MedicinalProductIngredientSpecifiedSubstance]] = empty_list()
    substance: Optional[MedicinalProductIngredientSubstance] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, True, None, False),
            ("substance", "substance", MedicinalProductIngredientSubstance, False, None, False),
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']