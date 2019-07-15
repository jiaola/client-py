#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceSpecification) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio

from . import domainresource

@dataclass
class SubstanceSpecification(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """
    resource_type: ClassVar[str] = "SubstanceSpecification"
    code: Optional[List[SubstanceSpecificationstr]] = empty_list()
    comment: Optional[str] = None
    description: Optional[str] = None
    domain: Optional[codeableconcept.CodeableConcept] = None
    identifier: Optional[identifier.Identifier] = None
    moiety: Optional[List[SubstanceSpecificationMoiety]] = empty_list()
    molecularWeight: Optional[List[SubstanceSpecificationStructureIsotopeMolecularWeight]] = empty_list()
    name: Optional[List[SubstanceSpecificationName]] = empty_list()
    nucleicAcid: Optional[fhirreference.FHIRReference] = None
    polymer: Optional[fhirreference.FHIRReference] = None
    property: Optional[List[SubstanceSpecificationProperty]] = empty_list()
    protein: Optional[fhirreference.FHIRReference] = None
    referenceInformation: Optional[fhirreference.FHIRReference] = None
    relationship: Optional[List[SubstanceSpecificationRelationship]] = empty_list()
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    sourceMaterial: Optional[fhirreference.FHIRReference] = None
    status: Optional[codeableconcept.CodeableConcept] = None
    structure: Optional[SubstanceSpecificationStructure] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecification, self).elementProperties()
        js.extend([
            ("code", "code", SubstanceSpecificationstr, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("moiety", "moiety", SubstanceSpecificationMoiety, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, True, None, False),
            ("name", "name", SubstanceSpecificationName, True, None, False),
            ("nucleicAcid", "nucleicAcid", fhirreference.FHIRReference, False, None, False),
            ("polymer", "polymer", fhirreference.FHIRReference, False, None, False),
            ("property", "property", SubstanceSpecificationProperty, True, None, False),
            ("protein", "protein", fhirreference.FHIRReference, False, None, False),
            ("referenceInformation", "referenceInformation", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", SubstanceSpecificationRelationship, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("sourceMaterial", "sourceMaterial", fhirreference.FHIRReference, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("structure", "structure", SubstanceSpecificationStructure, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SubstanceSpecificationMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationMoiety"
    amountQuantity: Optional[quantity.Quantity] = None
    amountString: Optional[str] = None
    identifier: Optional[identifier.Identifier] = None
    molecularFormula: Optional[str] = None
    name: Optional[str] = None
    opticalActivity: Optional[codeableconcept.CodeableConcept] = None
    role: Optional[codeableconcept.CodeableConcept] = None
    stereochemistry: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationMoiety, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationName(backboneelement.BackboneElement):
    """ Names applicable to this substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationName"
    domain: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    language: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: str = None
    official: Optional[List[SubstanceSpecificationNameOfficial]] = empty_list()
    preferred: Optional[bool] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[codeableconcept.CodeableConcept] = None
    synonym: Optional[List[SubstanceSpecificationName]] = empty_list()
    translation: Optional[List[SubstanceSpecificationName]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationName, self).elementProperties()
        js.extend([
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("official", "official", SubstanceSpecificationNameOfficial, True, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("synonym", "synonym", SubstanceSpecificationName, True, None, False),
            ("translation", "translation", SubstanceSpecificationName, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationNameOfficial(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationNameOfficial"
    authority: Optional[codeableconcept.CodeableConcept] = None
    date: Optional[fhirdate.FHIRDate] = None
    status: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationProperty(backboneelement.BackboneElement):
    """ General specifications for this substance, including how it is related to
    other substances.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationProperty"
    amountQuantity: Optional[quantity.Quantity] = None
    amountString: Optional[str] = None
    category: Optional[codeableconcept.CodeableConcept] = None
    code: Optional[codeableconcept.CodeableConcept] = None
    definingSubstanceCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    definingSubstanceReference: Optional[fhirreference.FHIRReference] = None
    parameters: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationProperty, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("definingSubstanceCodeableConcept", "definingSubstanceCodeableConcept", codeableconcept.CodeableConcept, False, "definingSubstance", False),
            ("definingSubstanceReference", "definingSubstanceReference", fhirreference.FHIRReference, False, "definingSubstance", False),
            ("parameters", "parameters", str, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationRelationship(backboneelement.BackboneElement):
    """ A link between this substance and another, with details of the relationship.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationRelationship"
    amountQuantity: Optional[quantity.Quantity] = None
    amountRange: Optional[range.Range] = None
    amountRatio: Optional[ratio.Ratio] = None
    amountRatioLowLimit: Optional[ratio.Ratio] = None
    amountString: Optional[str] = None
    amountType: Optional[codeableconcept.CodeableConcept] = None
    isDefining: Optional[bool] = None
    relationship: Optional[codeableconcept.CodeableConcept] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    substanceCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    substanceReference: Optional[fhirreference.FHIRReference] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationRelationship, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("amountRatioLowLimit", "amountRatioLowLimit", ratio.Ratio, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", False),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", False),
        ])
        return js

@dataclass
class SubstanceSpecificationStructure(backboneelement.BackboneElement):
    """ Structural information.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructure"
    isotope: Optional[List[SubstanceSpecificationStructureIsotope]] = empty_list()
    molecularFormula: Optional[str] = None
    molecularFormulaByMoiety: Optional[str] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None
    opticalActivity: Optional[codeableconcept.CodeableConcept] = None
    representation: Optional[List[SubstanceSpecificationStructureRepresentation]] = empty_list()
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    stereochemistry: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationStructure, self).elementProperties()
        js.extend([
            ("isotope", "isotope", SubstanceSpecificationStructureIsotope, True, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("representation", "representation", SubstanceSpecificationStructureRepresentation, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationStructureIsotope(backboneelement.BackboneElement):
    """ Applicable for single substances that contain a radionuclide or a non-
    natural isotopic ratio.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotope"
    halfLife: Optional[quantity.Quantity] = None
    identifier: Optional[identifier.Identifier] = None
    molecularWeight: Optional[SubstanceSpecificationStructureIsotopeMolecularWeight] = None
    name: Optional[codeableconcept.CodeableConcept] = None
    substitution: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotope, self).elementProperties()
        js.extend([
            ("halfLife", "halfLife", quantity.Quantity, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceSpecificationStructureIsotopeMolecularWeight, False, None, False),
            ("name", "name", codeableconcept.CodeableConcept, False, None, False),
            ("substitution", "substitution", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationStructureIsotopeMolecularWeight(backboneelement.BackboneElement):
    """ The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureIsotopeMolecularWeight"
    amount: Optional[quantity.Quantity] = None
    method: Optional[codeableconcept.CodeableConcept] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureIsotopeMolecularWeight, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationStructureRepresentation(backboneelement.BackboneElement):
    """ Molecular structural representation.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationStructureRepresentation"
    attachment: Optional[attachment.Attachment] = None
    representation: Optional[str] = None
    type: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationStructureRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

@dataclass
class SubstanceSpecificationstr(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """
    resource_type: ClassVar[str] = "SubstanceSpecificationstr"
    code: Optional[codeableconcept.CodeableConcept] = None
    comment: Optional[str] = None
    source: Optional[List[fhirreference.FHIRReference]] = empty_list()
    status: Optional[codeableconcept.CodeableConcept] = None
    statusDate: Optional[fhirdate.FHIRDate] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceSpecificationstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
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
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']