#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .range import Range
from .ratio import Ratio


@dataclass
class SubstanceSpecificationstr(BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationstr"
    code: Optional[CodeableConcept] = None
    comment: Optional[str] = None
    source: Optional[List[FHIRReference]] = empty_list()
    status: Optional[CodeableConcept] = None
    statusDate: Optional[FHIRDate] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationstr, self).elementProperties()
        js.extend([
            ("code", "code", CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("statusDate", "statusDate", FHIRDate, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationStructureRepresentation(BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureRepresentation"
    attachment: Optional[Attachment] = None
    representation: Optional[str] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationStructureIsotopeMolecularWeight(BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotopeMolecularWeight"
    amount: Optional[Quantity] = None
    method: Optional[CodeableConcept] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", Quantity, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationStructureIsotope(BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotope"
    halfLife: Optional[Quantity] = None
    identifier: Optional[Identifier] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None
    name: Optional[CodeableConcept] = None
    substitution: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("halfLife", "halfLife", Quantity, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("name", "name", CodeableConcept, False, None, False),
            ("substitution", "substitution", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationStructure(BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructure"
    isotope: Optional[List[SubstanceSpecificationStructureIsotope]] = empty_list()
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None
    opticalActivity: Optional[CodeableConcept] = None
    representation: Optional[List[SubstanceSpecificationStructureRepresentation]] = empty_list()
    source: Optional[List[FHIRReference]] = empty_list()
    stereochemistry: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("opticalActivity", "opticalActivity", CodeableConcept, False, None, False),
            ("representation", "representation", SubstanceSpecificationStructureRepresentation, True, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("stereochemistry", "stereochemistry", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationRelationship(BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationRelationship"
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountRatio: Optional[Ratio] = None
    amountRatioLowLimit: Optional[Ratio] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    isDefining: Optional[bool] = None
    relationship: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()
    substanceCodeableConcept: Optional[CodeableConcept] = None
    substanceReference: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationRelationship, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountRange", "amountRange", Range, False, "amount", False),
            ("amountRatio", "amountRatio", Ratio, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", Ratio, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("relationship", "relationship", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", CodeableConcept, False, "substance", False),
            ("substanceReference", "substanceReference", FHIRReference, False, "substance", False),
        ])
        return js


@dataclass
class SubstanceSpecificationProperty(BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationProperty"
    amountQuantity: Optional[Quantity] = None
    amountString: Optional[str] = None
    category: Optional[CodeableConcept] = None
    code: Optional[CodeableConcept] = None
    definingSubstanceCodeableConcept: Optional[CodeableConcept] = None
    definingSubstanceReference: Optional[FHIRReference] = None
    parameters: Optional[str] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("category", "category", CodeableConcept, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", CodeableConcept, False, "definingSubstance", False),
            ("definingSubstanceReference", "definingSubstanceReference", FHIRReference, False, "definingSubstance", False),
            ("parameters", "parameters", str, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationNameOfficial(BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationNameOfficial"
    authority: Optional[CodeableConcept] = None
    date: Optional[FHIRDate] = None
    status: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", CodeableConcept, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationName(BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationName"
    domain: Optional[List[CodeableConcept]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    language: Optional[List[CodeableConcept]] = empty_list()
    name: str = None
    official: Optional[List[SubstanceSpecificationNameOfficial]] = empty_list()
    preferred: Optional[bool] = None
    source: Optional[List[FHIRReference]] = empty_list()
    status: Optional[CodeableConcept] = None
    synonym: Optional[List[SubstanceSpecificationName]] = empty_list()
    translation: Optional[List[SubstanceSpecificationName]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationName, self).elementProperties()
        js.extend([
            ("domain", "domain", CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("language", "language", CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("official", "official", SubstanceSpecificationNameOfficial, True, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("synonym", "synonym", SubstanceSpecificationName, True, None, False),
            ("translation", "translation", SubstanceSpecificationName, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecificationMoiety(BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationMoiety"
    amountQuantity: Optional[Quantity] = None
    amountString: Optional[str] = None
    identifier: Optional[Identifier] = None
    molecularFormula: Optional[str] = None
    name: Optional[str] = None
    opticalActivity: Optional[CodeableConcept] = None
    role: Optional[CodeableConcept] = None
    stereochemistry: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", CodeableConcept, False, None, False),
            ("role", "role", CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSpecification(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceSpecification"
    code: Optional[List[SubstanceSpecificationstr]] = empty_list()
    comment: Optional[str] = None
    description: Optional[str] = None
    domain: Optional[CodeableConcept] = None
    identifier: Optional[Identifier] = None
    moiety: Optional[List[SubstanceSpecificationMoiety]] = empty_list()
    molecularWeight: Optional[List[SubstanceSpecificationStructureIsotopeMolecularWeight]] = empty_list()
    name: Optional[List[SubstanceSpecificationName]] = empty_list()
    nucleicAcid: Optional[FHIRReference] = None
    polymer: Optional[FHIRReference] = None
    property: Optional[List[SubstanceSpecificationProperty]] = empty_list()
    protein: Optional[FHIRReference] = None
    referenceInformation: Optional[FHIRReference] = None
    relationship: Optional[List[SubstanceSpecificationRelationship]] = empty_list()
    source: Optional[List[FHIRReference]] = empty_list()
    sourceMaterial: Optional[FHIRReference] = None
    status: Optional[CodeableConcept] = None
    structure: Optional[SubstanceSpecificationStructure] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("code", "code", SubstanceSpecificationstr, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("domain", "domain", CodeableConcept, False, None, False),
            ("identifier", "identifier", Identifier, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("name", "name", SubstanceSpecificationName, True, None, False),
            ("nucleicAcid", "nucleicAcid", FHIRReference, False, None, False),
            ("polymer", "polymer", FHIRReference, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("protein", "protein", FHIRReference, False, None, False),
            ("referenceInformation", "referenceInformation", FHIRReference, False, None, False),
            ("relationship", "relationship", SubstanceSpecificationRelationship, True, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("sourceMaterial", "sourceMaterial", FHIRReference, False, None, False),
            ("status", "status", CodeableConcept, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js