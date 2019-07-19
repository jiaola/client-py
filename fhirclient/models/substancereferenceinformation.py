#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation) on 2019-07-18.
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
from .quantity import Quantity
from .range import Range


@dataclass
class SubstanceReferenceInformationTarget(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationTarget"
    amountQuantity: Optional[Quantity] = None
    amountRange: Optional[Range] = None
    amountString: Optional[str] = None
    amountType: Optional[CodeableConcept] = None
    interaction: Optional[CodeableConcept] = None
    organism: Optional[CodeableConcept] = None
    organismType: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()
    target: Optional[Identifier] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", Quantity, False, "amount", False),
            ("amountRange", "amountRange", Range, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", CodeableConcept, False, None, False),
            ("interaction", "interaction", CodeableConcept, False, None, False),
            ("organism", "organism", CodeableConcept, False, None, False),
            ("organismType", "organismType", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("target", "target", Identifier, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationGeneElement(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGeneElement"
    element: Optional[Identifier] = None
    source: Optional[List[FHIRReference]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("element", "element", Identifier, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationGene(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationGene"
    gene: Optional[CodeableConcept] = None
    geneSequenceOrigin: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("gene", "gene", CodeableConcept, False, None, False),
            ("geneSequenceOrigin", "geneSequenceOrigin", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformationClassification(BackboneElement):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformationClassification"
    classification: Optional[CodeableConcept] = None
    domain: Optional[CodeableConcept] = None
    source: Optional[List[FHIRReference]] = empty_list()
    subtype: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", CodeableConcept, False, None, False),
            ("domain", "domain", CodeableConcept, False, None, False),
            ("source", "source", FHIRReference, True, None, False),
            ("subtype", "subtype", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class SubstanceReferenceInformation(DomainResource):
    """ Todo.
    """
    resource_type: ClassVar[str] = "SubstanceReferenceInformation"
    classification: Optional[List[SubstanceReferenceInformationClassification]] = empty_list()
    comment: Optional[str] = None
    gene: Optional[List[SubstanceReferenceInformationGene]] = empty_list()
    geneElement: Optional[List[SubstanceReferenceInformationGeneElement]] = empty_list()
    target: Optional[List[SubstanceReferenceInformationTarget]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("classification", "classification", SubstanceReferenceInformationClassification, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("gene", "gene", SubstanceReferenceInformationGene, True, None, False),
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, True, None, False),
            ("target", "target", SubstanceReferenceInformationTarget, True, None, False),
        ])
        return js