#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MolecularSequence) on 2019-07-15.
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
from . import quantity

from . import domainresource

@dataclass
class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.

    Raw data describing a biological sequence.
    """
    resource_type: ClassVar[str] = "MolecularSequence"
    coordinateSystem: int = None
    device: Optional[fhirreference.FHIRReference] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    observedSeq: Optional[str] = None
    patient: Optional[fhirreference.FHIRReference] = None
    performer: Optional[fhirreference.FHIRReference] = None
    pointer: Optional[List[fhirreference.FHIRReference]] = empty_list()
    quality: Optional[List[MolecularSequenceQuality]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    readCoverage: Optional[int] = None
    referenceSeq: Optional[MolecularSequenceReferenceSeq] = None
    repository: Optional[List[MolecularSequenceRepository]] = empty_list()
    specimen: Optional[fhirreference.FHIRReference] = None
    structureVariant: Optional[List[MolecularSequenceStructureVariant]] = empty_list()
    type: Optional[str] = None
    variant: Optional[List[MolecularSequenceVariant]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("type", "type", str, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.

    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    resource_type: ClassVar[str] = "MolecularSequenceQuality"
    end: Optional[int] = None
    fScore: Optional[float] = None
    gtFP: Optional[float] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    precision: Optional[float] = None
    queryFP: Optional[float] = None
    queryTP: Optional[float] = None
    recall: Optional[float] = None
    roc: Optional[MolecularSequenceQualityRoc] = None
    score: Optional[quantity.Quantity] = None
    standardSequence: Optional[codeableconcept.CodeableConcept] = None
    start: Optional[int] = None
    truthFN: Optional[float] = None
    truthTP: Optional[float] = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
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

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

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
class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.

    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    resource_type: ClassVar[str] = "MolecularSequenceReferenceSeq"
    chromosome: Optional[codeableconcept.CodeableConcept] = None
    genomeBuild: Optional[str] = None
    orientation: Optional[str] = None
    referenceSeqId: Optional[codeableconcept.CodeableConcept] = None
    referenceSeqPointer: Optional[fhirreference.FHIRReference] = None
    referenceSeqString: Optional[str] = None
    strand: Optional[str] = None
    windowEnd: Optional[int] = None
    windowStart: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
        ])
        return js

@dataclass
class MolecularSequenceRepository(backboneelement.BackboneElement):
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

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

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
class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.

    Information about chromosome structure variation.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariant"
    exact: Optional[bool] = None
    inner: Optional[MolecularSequenceStructureVariantInner] = None
    length: Optional[int] = None
    outer: Optional[MolecularSequenceStructureVariantOuter] = None
    variantType: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantInner"
    end: Optional[int] = None
    start: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js

@dataclass
class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """
    resource_type: ClassVar[str] = "MolecularSequenceStructureVariantOuter"
    end: Optional[int] = None
    start: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js

@dataclass
class MolecularSequenceVariant(backboneelement.BackboneElement):
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
    variantPointer: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']