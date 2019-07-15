#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceProtein) on 2019-07-15.
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

from . import domainresource

@dataclass
class SubstanceProtein(domainresource.DomainResource):
    """ A SubstanceProtein is defined as a single unit of a linear amino acid
    sequence, or a combination of subunits that are either covalently linked or
    have a defined invariant stoichiometric relationship. This includes all
    synthetic, recombinant and purified SubstanceProteins of defined sequence,
    whether the use is therapeutic or prophylactic. This set of elements will
    be used to describe albumins, coagulation factors, cytokines, growth
    factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids,
    recombinant vaccines, and immunomodulators.
    """
    resource_type: ClassVar[str] = "SubstanceProtein"
    disulfideLinkage: Optional[List[str]] = empty_list()
    numberOfSubunits: Optional[int] = None
    sequenceType: Optional[codeableconcept.CodeableConcept] = None
    subunit: Optional[List[SubstanceProteinSubunit]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceProtein, self).elementProperties()
        js.extend([
            ("disulfideLinkage", "disulfideLinkage", str, True, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("sequenceType", "sequenceType", codeableconcept.CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceProteinSubunit, True, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class SubstanceProteinSubunit(backboneelement.BackboneElement):
    """ This subclause refers to the description of each subunit constituting the
    SubstanceProtein. A subunit is a linear sequence of amino acids linked
    through peptide bonds. The Subunit information shall be provided when the
    finished SubstanceProtein is a complex of multiple sequences; subunits are
    not used to delineate domains within a single sequence. Subunits are listed
    in order of decreasing length; sequences of the same length will be ordered
    by decreasing molecular weight; subunits that have identical sequences will
    be repeated multiple times.
    """
    resource_type: ClassVar[str] = "SubstanceProteinSubunit"
    cTerminalModification: Optional[str] = None
    cTerminalModificationId: Optional[identifier.Identifier] = None
    length: Optional[int] = None
    nTerminalModification: Optional[str] = None
    nTerminalModificationId: Optional[identifier.Identifier] = None
    sequence: Optional[str] = None
    sequenceAttachment: Optional[attachment.Attachment] = None
    subunit: Optional[int] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(SubstanceProteinSubunit, self).elementProperties()
        js.extend([
            ("cTerminalModification", "cTerminalModification", str, False, None, False),
            ("cTerminalModificationId", "cTerminalModificationId", identifier.Identifier, False, None, False),
            ("length", "length", int, False, None, False),
            ("nTerminalModification", "nTerminalModification", str, False, None, False),
            ("nTerminalModificationId", "nTerminalModificationId", identifier.Identifier, False, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", attachment.Attachment, False, None, False),
            ("subunit", "subunit", int, False, None, False),
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