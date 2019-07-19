#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2019-07-18.
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


@dataclass
class MolecularSequenceVariant(BackboneElement):
    """ Variant in sequence.

    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    resource_type: ClassVar[str] = "MolecularSequenceVariant"
    cigar: Optional[str] = None
    end: Optional[int] = None
    observedAllele: Optional[str] = None
    referenceAllele: Optional[str] = None
    start: Optional[int] = None
    variantPointer: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
            ("variantPointer", "variantPointer", FHIRReference, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceStructureVariantOuter(BackboneElement):
    """ Structural variant outer.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantOuter"
    end: Optional[int] = None
    start: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceStructureVariantInner(BackboneElement):
    """ Structural variant inner.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantInner"
    end: Optional[int] = None
    start: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceStructureVariant(BackboneElement):
    """ Structural variant.

    Information about chromosome structure variation.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariant"
    exact: Optional[bool] = None
    inner: Optional[MolecularSequenceStructureVariantInner] = None
    length: Optional[int] = None
    outer: Optional[MolecularSequenceStructureVariantOuter] = None
    variantType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("variantType", "variantType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceRepository(BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.

    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    resource_type: ClassVar[str] = "MolecularSequenceRepository"
    datasetId: Optional[str] = None
    name: Optional[str] = None
    readsetId: Optional[str] = None
    type: str = None
    url: Optional[str] = None
    variantsetId: Optional[str] = None

    def elementProperties(self):
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceReferenceSeq(BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    resource_type: ClassVar[str] = "MolecularSequenceReferenceSeq"
    chromosome: Optional[CodeableConcept] = None
    genomeBuild: Optional[str] = None
    orientation: Optional[str] = None
    referenceSeqId: Optional[CodeableConcept] = None
    referenceSeqPointer: Optional[FHIRReference] = None
    referenceSeqString: Optional[str] = None
    strand: Optional[str] = None
    windowEnd: Optional[int] = None
    windowStart: Optional[int] = None

    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
        ])
        return js


@dataclass
class MolecularSequenceQualityRoc(BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.

    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    resource_type: ClassVar[str] = "MolecularSequenceQualityRoc"
    fMeasure: Optional[List[float]] = empty_list()
    numFN: Optional[List[int]] = empty_list()
    numFP: Optional[List[int]] = empty_list()
    numTP: Optional[List[int]] = empty_list()
    precision: Optional[List[float]] = empty_list()
    score: Optional[List[int]] = empty_list()
    sensitivity: Optional[List[float]] = empty_list()

    def elementProperties(self):
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("fMeasure", "fMeasure", float, True, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("precision", "precision", float, True, None, False),
            ("score", "score", int, True, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
        ])
        return js


@dataclass
class MolecularSequenceQuality(BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    resource_type: ClassVar[str] = "MolecularSequenceQuality"
    end: Optional[int] = None
    fScore: Optional[float] = None
    gtFP: Optional[float] = None
    method: Optional[CodeableConcept] = None
    precision: Optional[float] = None
    queryFP: Optional[float] = None
    queryTP: Optional[float] = None
    recall: Optional[float] = None
    roc: Optional[MolecularSequenceQualityRoc] = None
    score: Optional[Quantity] = None
    standardSequence: Optional[CodeableConcept] = None
    start: Optional[int] = None
    truthFN: Optional[float] = None
    truthTP: Optional[float] = None
    type: str = None

    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("method", "method", CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("score", "score", Quantity, False, None, False),
            ("standardSequence", "standardSequence", CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


@dataclass
class MolecularSequence(DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """
    resource_type: ClassVar[str] = "MolecularSequence"
    coordinateSystem: int = None
    device: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    observedSeq: Optional[str] = None
    patient: Optional[FHIRReference] = None
    performer: Optional[FHIRReference] = None
    pointer: Optional[List[FHIRReference]] = empty_list()
    quality: Optional[List[MolecularSequenceQuality]] = empty_list()
    quantity: Optional[Quantity] = None
    readCoverage: Optional[int] = None
    referenceSeq: Optional[MolecularSequenceReferenceSeq] = None
    repository: Optional[List[MolecularSequenceRepository]] = empty_list()
    specimen: Optional[FHIRReference] = None
    structureVariant: Optional[List[MolecularSequenceStructureVariant]] = empty_list()
    type: Optional[str] = None
    variant: Optional[List[MolecularSequenceVariant]] = empty_list()

    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("device", "device", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", FHIRReference, False, None, False),
            ("performer", "performer", FHIRReference, False, None, False),
            ("pointer", "pointer", FHIRReference, True, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("quantity", "quantity", Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("specimen", "specimen", FHIRReference, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("type", "type", str, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
        ])
        return js