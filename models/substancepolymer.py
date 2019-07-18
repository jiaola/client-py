#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstancePolymer) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import substanceamount

from . import backboneelement

@dataclass
class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"
    attachment: Optional[attachment.Attachment] = None
    representation: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"
    amount: Optional[substanceamount.SubstanceAmount] = None
    degree: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("degree", "degree", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnit"
    amount: Optional[substanceamount.SubstanceAmount] = None
    degreeOfPolymerisation: Optional[List[SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation]] = empty_list()
    orientationOfPolymerisation: Optional[codeableconcept.CodeableConcept] = None
    repeatUnit: Optional[str] = None
    structuralRepresentation: Optional[List[SubstancePolymerRepeatRepeatUnitStructuralRepresentation]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnit, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("degreeOfPolymerisation", "degreeOfPolymerisation", SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, True, None, False),
            ("orientationOfPolymerisation", "orientationOfPolymerisation", codeableconcept.CodeableConcept, False, None, False),
            ("repeatUnit", "repeatUnit", str, False, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstancePolymerRepeatRepeatUnitStructuralRepresentation, True, None, False),
        ])
        return js

@dataclass
class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeat"
    averageMolecularFormula: Optional[str] = None
    numberOfUnits: Optional[int] = None
    repeatUnit: Optional[List[SubstancePolymerRepeatRepeatUnit]] = empty_list()
    repeatUnitAmountType: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerRepeat, self).elementProperties()
        js.extend([
            ("averageMolecularFormula", "averageMolecularFormula", str, False, None, False),
            ("numberOfUnits", "numberOfUnits", int, False, None, False),
            ("repeatUnit", "repeatUnit", SubstancePolymerRepeatRepeatUnit, True, None, False),
            ("repeatUnitAmountType", "repeatUnitAmountType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSetStartingMaterial"
    amount: Optional[substanceamount.SubstanceAmount] = None
    isDefining: Optional[bool] = None
    material: Optional[codeableconcept.CodeableConcept] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSetStartingMaterial, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSet"
    ratioType: Optional[codeableconcept.CodeableConcept] = None
    startingMaterial: Optional[List[SubstancePolymerMonomerSetStartingMaterial]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSet, self).elementProperties()
        js.extend([
            ("ratioType", "ratioType", codeableconcept.CodeableConcept, False, None, False),
            ("startingMaterial", "startingMaterial", SubstancePolymerMonomerSetStartingMaterial, True, None, False),
        ])
        return js

from . import domainresource

@dataclass
class SubstancePolymer(domainresource.DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymer"
    class_fhir: Optional[codeableconcept.CodeableConcept] = None
    copolymerConnectivity: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    geometry: Optional[codeableconcept.CodeableConcept] = None
    modification: Optional[List[str]] = empty_list()
    monomerSet: Optional[List[SubstancePolymerMonomerSet]] = empty_list()
    repeat: Optional[List[SubstancePolymerRepeat]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstancePolymer, self).elementProperties()
        js.extend([
            ("class_fhir", "class", codeableconcept.CodeableConcept, False, None, False),
            ("copolymerConnectivity", "copolymerConnectivity", codeableconcept.CodeableConcept, True, None, False),
            ("geometry", "geometry", codeableconcept.CodeableConcept, False, None, False),
            ("modification", "modification", str, True, None, False),
            ("monomerSet", "monomerSet", SubstancePolymerMonomerSet, True, None, False),
            ("repeat", "repeat", SubstancePolymerRepeat, True, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import substanceamount
except ImportError:
    substanceamount = sys.modules[__package__ + '.substanceamount']