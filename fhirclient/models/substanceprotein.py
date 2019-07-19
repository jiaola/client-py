#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceProtein) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier


@dataclass
class SubstanceProteinSubunit(BackboneElement):
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
    cTerminalModificationId: Optional[Identifier] = None
    length: Optional[int] = None
    nTerminalModification: Optional[str] = None
    nTerminalModificationId: Optional[Identifier] = None
    sequence: Optional[str] = None
    sequenceAttachment: Optional[Attachment] = None
    subunit: Optional[int] = None

    def elementProperties(self):
        js = super(SubstanceProteinSubunit, self).elementProperties()
        js.extend([
            ("cTerminalModification", "cTerminalModification", str, False, None, False),
            ("cTerminalModificationId", "cTerminalModificationId", Identifier, False, None, False),
            ("length", "length", int, False, None, False),
            ("nTerminalModification", "nTerminalModification", str, False, None, False),
            ("nTerminalModificationId", "nTerminalModificationId", Identifier, False, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", Attachment, False, None, False),
            ("subunit", "subunit", int, False, None, False),
        ])
        return js


@dataclass
class SubstanceProtein(DomainResource):
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
    sequenceType: Optional[CodeableConcept] = None
    subunit: Optional[List[SubstanceProteinSubunit]] = empty_list()

    def elementProperties(self):
        js = super(SubstanceProtein, self).elementProperties()
        js.extend([
            ("disulfideLinkage", "disulfideLinkage", str, True, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("sequenceType", "sequenceType", CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceProteinSubunit, True, None, False),
        ])
        return js