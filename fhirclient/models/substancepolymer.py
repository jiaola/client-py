#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstancePolymer) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .substanceamount import SubstanceAmount


@dataclass
class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"
    attachment: Optional[Attachment] = None
    representation: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"
    amount: Optional[SubstanceAmount] = None
    degree: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).elementProperties()
        js.extend([
            ("amount", "amount", SubstanceAmount, False, None, False),
            ("degree", "degree", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeatRepeatUnit(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeatRepeatUnit"
    amount: Optional[SubstanceAmount] = None
    degreeOfPolymerisation: Optional[List[SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation]] = empty_list()
    orientationOfPolymerisation: Optional[CodeableConcept] = None
    repeatUnit: Optional[str] = None
    structuralRepresentation: Optional[List[SubstancePolymerRepeatRepeatUnitStructuralRepresentation]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnit, self).elementProperties()
        js.extend([
            ("amount", "amount", SubstanceAmount, False, None, False),
            ("degreeOfPolymerisation", "degreeOfPolymerisation", SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, True, None, False),
            ("orientationOfPolymerisation", "orientationOfPolymerisation", CodeableConcept, False, None, False),
            ("repeatUnit", "repeatUnit", str, False, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstancePolymerRepeatRepeatUnitStructuralRepresentation, True, None, False),
        ])
        return js


@dataclass
class SubstancePolymerRepeat(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerRepeat"
    averageMolecularFormula: Optional[str] = None
    numberOfUnits: Optional[int] = None
    repeatUnit: Optional[List[SubstancePolymerRepeatRepeatUnit]] = empty_list()
    repeatUnitAmountType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstancePolymerRepeat, self).elementProperties()
        js.extend([
            ("averageMolecularFormula", "averageMolecularFormula", str, False, None, False),
            ("numberOfUnits", "numberOfUnits", int, False, None, False),
            ("repeatUnit", "repeatUnit", SubstancePolymerRepeatRepeatUnit, True, None, False),
            ("repeatUnitAmountType", "repeatUnitAmountType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerMonomerSetStartingMaterial(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSetStartingMaterial"
    amount: Optional[SubstanceAmount] = None
    isDefining: Optional[bool] = None
    material: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSetStartingMaterial, self).elementProperties()
        js.extend([
            ("amount", "amount", SubstanceAmount, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("material", "material", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstancePolymerMonomerSet(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymerMonomerSet"
    ratioType: Optional[CodeableConcept] = None
    startingMaterial: Optional[List[SubstancePolymerMonomerSetStartingMaterial]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymerMonomerSet, self).elementProperties()
        js.extend([
            ("ratioType", "ratioType", CodeableConcept, False, None, False),
            ("startingMaterial", "startingMaterial", SubstancePolymerMonomerSetStartingMaterial, True, None, False),
        ])
        return js


@dataclass
class SubstancePolymer(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstancePolymer"
    class_fhir: Optional[CodeableConcept] = None
    copolymerConnectivity: Optional[List[CodeableConcept]] = empty_list()
    geometry: Optional[CodeableConcept] = None
    modification: Optional[List[str]] = empty_list()
    monomerSet: Optional[List[SubstancePolymerMonomerSet]] = empty_list()
    repeat: Optional[List[SubstancePolymerRepeat]] = empty_list()

    def elementProperties(self):
        js = super(SubstancePolymer, self).elementProperties()
        js.extend([
            ("class_fhir", "class", CodeableConcept, False, None, False),
            ("copolymerConnectivity", "copolymerConnectivity", CodeableConcept, True, None, False),
            ("geometry", "geometry", CodeableConcept, False, None, False),
            ("modification", "modification", str, True, None, False),
            ("monomerSet", "monomerSet", SubstancePolymerMonomerSet, True, None, False),
            ("repeat", "repeat", SubstancePolymerRepeat, True, None, False),
        ])
        return js