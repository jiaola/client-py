#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid) on 2019-07-18.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import attachment
from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import identifier

from . import backboneelement

@dataclass
class SubstanceNucleicAcidSubunitSugar(backboneelement.BackboneElement):
    """ 5.3.6.8.1 Sugar ID (Mandatory).
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitSugar"
    identifier: Optional[identifier.Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitSugar, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js

@dataclass
class SubstanceNucleicAcidSubunitLinkage(backboneelement.BackboneElement):
    """ The linkages between sugar residues will also be captured.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunitLinkage"
    connectivity: Optional[str] = None
    identifier: Optional[identifier.Identifier] = None
    name: Optional[str] = None
    residueSite: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitLinkage, self).elementProperties()
        js.extend([
            ("connectivity", "connectivity", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js

@dataclass
class SubstanceNucleicAcidSubunit(backboneelement.BackboneElement):
    """ Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcidSubunit"
    fivePrime: Optional[codeableconcept.CodeableConcept] = None
    length: Optional[int] = None
    linkage: Optional[List[SubstanceNucleicAcidSubunitLinkage]] = empty_list()
    sequence: Optional[str] = None
    sequenceAttachment: Optional[attachment.Attachment] = None
    subunit: Optional[int] = None
    sugar: Optional[List[SubstanceNucleicAcidSubunitSugar]] = empty_list()
    threePrime: Optional[codeableconcept.CodeableConcept] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunit, self).elementProperties()
        js.extend([
            ("fivePrime", "fivePrime", codeableconcept.CodeableConcept, False, None, False),
            ("length", "length", int, False, None, False),
            ("linkage", "linkage", SubstanceNucleicAcidSubunitLinkage, True, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", attachment.Attachment, False, None, False),
            ("subunit", "subunit", int, False, None, False),
            ("sugar", "sugar", SubstanceNucleicAcidSubunitSugar, True, None, False),
            ("threePrime", "threePrime", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js

from . import domainresource

@dataclass
class SubstanceNucleicAcid(domainresource.DomainResource):
    """ Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """
    resource_type: ClassVar[str] = "SubstanceNucleicAcid"
    areaOfHybridisation: Optional[str] = None
    numberOfSubunits: Optional[int] = None
    oligoNucleotideType: Optional[codeableconcept.CodeableConcept] = None
    sequenceType: Optional[codeableconcept.CodeableConcept] = None
    subunit: Optional[List[SubstanceNucleicAcidSubunit]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceNucleicAcid, self).elementProperties()
        js.extend([
            ("areaOfHybridisation", "areaOfHybridisation", str, False, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("oligoNucleotideType", "oligoNucleotideType", codeableconcept.CodeableConcept, False, None, False),
            ("sequenceType", "sequenceType", codeableconcept.CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceNucleicAcidSubunit, True, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']