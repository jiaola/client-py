#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/ClinicalProfile) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .quantity import Quantity
from .ratio import Ratio


@dataclass
class ClinicalProfileMedicationDosage(BackboneElement):
    """ Details of how medication was taken.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedicationDosage"

    text: Optional[str] = None
    site: Optional[List[CodeableConcept]] = None
    route: Optional[List[CodeableConcept]] = None
    method: Optional[List[CodeableConcept]] = None
    dose: Optional[List[Quantity]] = None
    rateRatio: Optional[Ratio] = field(default=None, metadata=dict(one_of_many='rate',))
    rateQuantity: Optional[Quantity] = field(default=None, metadata=dict(one_of_many='rate',))


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry(BackboneElement):
    """ Correlation entry.

    List of correlated phenotypes in descending order of the absolute value of
    the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry"

    code: CodeableConcept = None
    coefficient: float = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry"

    code: List[CodeableConcept] = field(default_factory=list)
    coefficient: float = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds(BackboneElement):
    """ Medication code(s).
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds"

    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry"

    meds: List[ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntryMeds] = field(default_factory=list)
    coefficient: float = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry(BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry"

    code: CodeableConcept = None
    coefficient: float = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabsEntry(BackboneElement):
    """ Correlated lab.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabsEntry"

    labcode: List[CodeableConcept] = field(default_factory=list)
    coefficient: float = None


@dataclass
class ClinicalProfileLabScalarDistributionDecile(BackboneElement):
    """ Decile partitions.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionDecile"

    nth: int = None
    value: float = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabs(BackboneElement):
    """ Correlated laboratory tests.

    An ordered list of the laboratory tests  that are most closely correlated.
    This list can be limited by the top "n" labs and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabs"

    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedLabsEntry]] = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnoses(BackboneElement):
    """ Correlated diagnosies.

    An ordered list of  the diagnoses  that are most closely correlated.  This
    list can be limited by the top "n" diagnoses and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnoses"

    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry]] = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedications(BackboneElement):
    """ Correlated medications.

    An ordered list of  the medications  that are most closely correlated.
    This list can be limited by the top "n" medications and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedications"

    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry]] = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProcedures(BackboneElement):
    """ Correlated procedures.

    An ordered list of  the procedures  that are most closely correlated.  This
    list can be limited by the top "n" procedures and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProcedures"

    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry]] = None


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypes(BackboneElement):
    """ Correlated phenotypes.

    An ordered list of  the phenotypes  that are most closely correlated.  This
    list can be limited by the top "n" phenotypes and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypes"

    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry]] = None


@dataclass
class ClinicalProfileLabScalarDistribution(BackboneElement):
    """ Scalar sample summary.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistribution"

    units: Quantity = None
    min: float = None
    max: float = None
    mean: float = None
    median: float = None
    stdDev: float = None
    decile: Optional[List[ClinicalProfileLabScalarDistributionDecile]] = None
    normalizedHigh: Optional[float] = None
    normalizedLow: Optional[float] = None
    fractionAboveNormal: Optional[float] = None
    fractionBelowNormal: Optional[float] = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None


@dataclass
class ClinicalProfileLab(BackboneElement):
    """ Laboratory profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLab"

    code: List[CodeableConcept] = field(default_factory=list)
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: Optional[float] = None
    scalarDistribution: Optional[ClinicalProfileLabScalarDistribution] = None


@dataclass
class ClinicalProfileMedication(BackboneElement):
    """ Medication profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedication"

    category: Optional[CodeableConcept] = None
    medicationCodeableConcept: CodeableConcept = field(default=None, metadata=dict(one_of_many='medication',))
    medicationReference: FHIRReference = field(default=None, metadata=dict(one_of_many='medication',))
    dosage: Optional[ClinicalProfileMedicationDosage] = None
    treatementDuration: Optional[float] = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None


@dataclass
class ClinicalProfileDiagnosis(BackboneElement):
    """ Diagnosis profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileDiagnosis"

    code: List[CodeableConcept] = field(default_factory=list)
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None


@dataclass
class ClinicalProfileProcedure(BackboneElement):
    """ Procedure profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileProcedure"

    code: List[CodeableConcept] = field(default_factory=list)
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None


@dataclass
class ClinicalProfileHpo(BackboneElement):
    """ HPO Profile Entry.

    Phenotypic description.
    """
    resource_type: ClassVar[str] = "ClinicalProfileHpo"

    code: List[CodeableConcept] = field(default_factory=list)
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None


@dataclass
class ClinicalProfile(DomainResource):
    """ Results of a measure evaluation.

    Clinical Profiles summarize and demonstrate the features of a population.
    """
    resource_type: ClassVar[str] = "ClinicalProfile"

    identifier: Optional[List[Identifier]] = None
    status: str = None
    population: FHIRReference = None
    cohort: FHIRReference = None
    date: Optional[FHIRDate] = None
    source: Optional[List[Identifier]] = None
    reporter: FHIRReference = None
    lab: Optional[List[ClinicalProfileLab]] = None
    medication: Optional[List[ClinicalProfileMedication]] = None
    diagnosis: Optional[List[ClinicalProfileDiagnosis]] = None
    procedure: Optional[List[ClinicalProfileProcedure]] = None
    hpo: Optional[List[ClinicalProfileHpo]] = None