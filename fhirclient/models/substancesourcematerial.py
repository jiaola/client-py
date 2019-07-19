#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .identifier import Identifier


@dataclass
class SubstanceSourceMaterialPartDescription(BackboneElement):
    """ To do.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialPartDescription"
    part: Optional[CodeableConcept] = None
    partLocation: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialPartDescription, self).elementProperties()
        js.extend([
            ("part", "part", CodeableConcept, False, None, False),
            ("partLocation", "partLocation", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterialOrganismOrganismGeneral(BackboneElement):
    """ 4.9.13.7.1 Kingdom (Conditional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismOrganismGeneral"
    class_fhir: Optional[CodeableConcept] = None
    kingdom: Optional[CodeableConcept] = None
    order: Optional[CodeableConcept] = None
    phylum: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismOrganismGeneral, self).elementProperties()
        js.extend([
            ("class_fhir", "class", CodeableConcept, False, None, False),
            ("kingdom", "kingdom", CodeableConcept, False, None, False),
            ("order", "order", CodeableConcept, False, None, False),
            ("phylum", "phylum", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterialOrganismHybrid(BackboneElement):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismHybrid"
    hybridType: Optional[CodeableConcept] = None
    maternalOrganismId: Optional[str] = None
    maternalOrganismName: Optional[str] = None
    paternalOrganismId: Optional[str] = None
    paternalOrganismName: Optional[str] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismHybrid, self).elementProperties()
        js.extend([
            ("hybridType", "hybridType", CodeableConcept, False, None, False),
            ("maternalOrganismId", "maternalOrganismId", str, False, None, False),
            ("maternalOrganismName", "maternalOrganismName", str, False, None, False),
            ("paternalOrganismId", "paternalOrganismId", str, False, None, False),
            ("paternalOrganismName", "paternalOrganismName", str, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterialOrganismAuthor(BackboneElement):
    """ 4.9.13.6.1 Author type (Conditional).
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganismAuthor"
    authorDescription: Optional[str] = None
    authorType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganismAuthor, self).elementProperties()
        js.extend([
            ("authorDescription", "authorDescription", str, False, None, False),
            ("authorType", "authorType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterialOrganism(BackboneElement):
    """ This subclause describes the organism which the substance is derived from.
    For vaccines, the parent organism shall be specified based on these
    subclause elements. As an example, full taxonomy will be described for the
    Substance Name: ., Leaf.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialOrganism"
    author: Optional[List[SubstanceSourceMaterialOrganismAuthor]] = empty_list()
    family: Optional[CodeableConcept] = None
    genus: Optional[CodeableConcept] = None
    hybrid: Optional[SubstanceSourceMaterialOrganismHybrid] = None
    intraspecificDescription: Optional[str] = None
    intraspecificType: Optional[CodeableConcept] = None
    organismGeneral: Optional[SubstanceSourceMaterialOrganismOrganismGeneral] = None
    species: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialOrganism, self).elementProperties()
        js.extend([
            ("author", "author", SubstanceSourceMaterialOrganismAuthor, True, None, False),
            ("family", "family", CodeableConcept, False, None, False),
            ("genus", "genus", CodeableConcept, False, None, False),
            ("hybrid", "hybrid", SubstanceSourceMaterialOrganismHybrid, False, None, False),
            ("intraspecificDescription", "intraspecificDescription", str, False, None, False),
            ("intraspecificType", "intraspecificType", CodeableConcept, False, None, False),
            ("organismGeneral", "organismGeneral", SubstanceSourceMaterialOrganismOrganismGeneral, False, None, False),
            ("species", "species", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterialFractionDescription(BackboneElement):
    """ Many complex materials are fractions of parts of plants, animals, or
    minerals. Fraction elements are often necessary to define both Substances
    and Specified Group 1 Substances. For substances derived from Plants,
    fraction information will be captured at the Substance information level (
    . Oils, Juices and Exudates). Additional information for Extracts, such as
    extraction solvent composition, will be captured at the Specified Substance
    Group 1 information level. For plasma-derived products fraction information
    will be captured at the Substance and the Specified Substance Group 1
    levels.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterialFractionDescription"
    fraction: Optional[str] = None
    materialType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterialFractionDescription, self).elementProperties()
        js.extend([
            ("fraction", "fraction", str, False, None, False),
            ("materialType", "materialType", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class SubstanceSourceMaterial(DomainResource):
    """ Source material shall capture information on the taxonomic and anatomical
    origins as well as the fraction of a material that can result in or can be
    modified to form a substance. This set of data elements shall be used to
    define polymer substances isolated from biological matrices. Taxonomic and
    anatomical origins shall be described using a controlled vocabulary as
    required. This information is captured for naturally derived polymers ( .
    starch) and structurally diverse substances. For Organisms belonging to the
    Kingdom Plantae the Substance level defines the fresh material of a single
    species or infraspecies, the Herbal Drug and the Herbal preparation. For
    Herbal preparations, the fraction information will be captured at the
    Substance information level and additional information for herbal extracts
    will be captured at the Specified Substance Group 1 information level. See
    for further explanation the Substance Class: Structurally Diverse and the
    herbal annex.
    """
    resource_type: ClassVar[str] = "SubstanceSourceMaterial"
    countryOfOrigin: Optional[List[CodeableConcept]] = empty_list()
    developmentStage: Optional[CodeableConcept] = None
    fractionDescription: Optional[List[SubstanceSourceMaterialFractionDescription]] = empty_list()
    geographicalLocation: Optional[List[str]] = empty_list()
    organism: Optional[SubstanceSourceMaterialOrganism] = None
    organismId: Optional[Identifier] = None
    organismName: Optional[str] = None
    parentSubstanceId: Optional[List[Identifier]] = empty_list()
    parentSubstanceName: Optional[List[str]] = empty_list()
    partDescription: Optional[List[SubstanceSourceMaterialPartDescription]] = empty_list()
    sourceMaterialClass: Optional[CodeableConcept] = None
    sourceMaterialState: Optional[CodeableConcept] = None
    sourceMaterialType: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(SubstanceSourceMaterial, self).elementProperties()
        js.extend([
            ("countryOfOrigin", "countryOfOrigin", CodeableConcept, True, None, False),
            ("developmentStage", "developmentStage", CodeableConcept, False, None, False),
            ("fractionDescription", "fractionDescription", SubstanceSourceMaterialFractionDescription, True, None, False),
            ("geographicalLocation", "geographicalLocation", str, True, None, False),
            ("organism", "organism", SubstanceSourceMaterialOrganism, False, None, False),
            ("organismId", "organismId", Identifier, False, None, False),
            ("organismName", "organismName", str, False, None, False),
            ("parentSubstanceId", "parentSubstanceId", Identifier, True, None, False),
            ("parentSubstanceName", "parentSubstanceName", str, True, None, False),
            ("partDescription", "partDescription", SubstanceSourceMaterialPartDescription, True, None, False),
            ("sourceMaterialClass", "sourceMaterialClass", CodeableConcept, False, None, False),
            ("sourceMaterialState", "sourceMaterialState", CodeableConcept, False, None, False),
            ("sourceMaterialType", "sourceMaterialType", CodeableConcept, False, None, False),
        ])
        return js