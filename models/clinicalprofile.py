#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-baa72e6471 (http://hl7.org/fhir/StructureDefinition/ClinicalProfile) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


from . import domainresource

@dataclass
class ClinicalProfile(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    Clinical Profiles summarize and demonstrate the features of a population.
    """
    resource_type: ClassVar[str] = "ClinicalProfile"
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    status: str = None
    population:fhirreference.FHIRReference = None
    cohort:fhirreference.FHIRReference = None
    date: Optional[fhirdate.FHIRDate] = None
    source: Optional[List[identifier.Identifier]] = empty_list()
    reporter:fhirreference.FHIRReference = None
    lab: Optional[List[ClinicalProfileLab]] = empty_list()
    medication: Optional[List[ClinicalProfileMedication]] = empty_list()
    diagnosis: Optional[List[ClinicalProfileDiagnosis]] = empty_list()
    procedure: Optional[List[ClinicalProfileProcedure]] = empty_list()
    hpo: Optional[List[ClinicalProfileHpo]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.identifier = None
#        """ Additional identifier for the ClinicalProfile.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.status = None
#        """ complete | draft | error.
#        Type `str`
#
#. """
#
#
#        self.population = None
#        """ The base population against which this profile was generated.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.cohort = None
#        """ The cohort within the population that this profile represents.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ When the profile was generated.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.source = None
#        """ Identifier(s) from where the profile was acquired.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reporter = None
#        """ Who is reporting the data.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.lab = None
#        """ Laboratory profile entry.
#        List of `ClinicalProfileLab` items
#
# (represented as `dict` in JSON). """
#
#
#        self.medication = None
#        """ Medication profile entry.
#        List of `ClinicalProfileMedication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.diagnosis = None
#        """ Diagnosis profile entry.
#        List of `ClinicalProfileDiagnosis` items
#
# (represented as `dict` in JSON). """
#
#
#        self.procedure = None
#        """ Procedure profile entry.
#        List of `ClinicalProfileProcedure` items
#
# (represented as `dict` in JSON). """
#
#
#        self.hpo = None
#        """ HPO Profile Entry.
#        List of `ClinicalProfileHpo` items
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfile, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", str, False, None, True),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("cohort", "cohort", fhirreference.FHIRReference, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("source", "source", identifier.Identifier, True, None, False),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, True),
            ("lab", "lab", ClinicalProfileLab, True, None, False),
            ("medication", "medication", ClinicalProfileMedication, True, None, False),
            ("diagnosis", "diagnosis", ClinicalProfileDiagnosis, True, None, False),
            ("procedure", "procedure", ClinicalProfileProcedure, True, None, False),
            ("hpo", "hpo", ClinicalProfileHpo, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


from . import backboneelement

@dataclass
class ClinicalProfileLab(backboneelement.BackboneElement):
    """ Laboratory profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLab"
    code: List[codeableconcept.CodeableConcept] = empty_list()
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: Optional[float] = None
    scalarDistribution: Optional[ClinicalProfileLabScalarDistribution] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Lab code (LOINC).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.count = None
#        """ Total number of lab tests.
#        Type `int`
#
#. """
#
#
#        self.frequencyPerYear = None
#        """ Frequency of this lab ordered/reported per patient per year.
#        Type `float`
#
#. """
#
#
#        self.fractionOfSubjects = None
#        """ Fraction of subjects with this lab.
#        Type `float`
#
#. """
#
#
#        self.scalarDistribution = None
#        """ Scalar sample summary.
#        Type `ClinicalProfileLabScalarDistribution`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLab, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLab, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("count", "count", int, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, False),
            ("scalarDistribution", "scalarDistribution", ClinicalProfileLabScalarDistribution, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistribution(backboneelement.BackboneElement):
    """ Scalar sample summary.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistribution"
    units:quantity.Quantity = None
    min: float = None
    max: float = None
    mean: float = None
    median: float = None
    stdDev: float = None
    decile: Optional[List[ClinicalProfileLabScalarDistributionDecile]] = empty_list()
    normalizedHigh: Optional[float] = None
    normalizedLow: Optional[float] = None
    fractionAboveNormal: Optional[float] = None
    fractionBelowNormal: Optional[float] = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.units = None
#        """ Units of scalar result.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.min = None
#        """ Minimum value.
#        Type `float`
#
#. """
#
#
#        self.max = None
#        """ Maximum value.
#        Type `float`
#
#. """
#
#
#        self.mean = None
#        """ Mean.
#        Type `float`
#
#. """
#
#
#        self.median = None
#        """ Median.
#        Type `float`
#
#. """
#
#
#        self.stdDev = None
#        """ Standard deviation.
#        Type `float`
#
#. """
#
#
#        self.decile = None
#        """ Decile partitions.
#        List of `ClinicalProfileLabScalarDistributionDecile` items
#
# (represented as `dict` in JSON). """
#
#
#        self.normalizedHigh = None
#        """ Normalize high normal range.
#        Type `float`
#
#. """
#
#
#        self.normalizedLow = None
#        """ Normalize low normal range.
#        Type `float`
#
#. """
#
#
#        self.fractionAboveNormal = None
#        """ Fraction of samples above normalized normal range.
#        Type `float`
#
#. """
#
#
#        self.fractionBelowNormal = None
#        """ Fraction of samples below normalized normal range.
#        Type `float`
#
#. """
#
#
#        self.correlatedLabs = None
#        """ Correlated laboratory tests.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedDiagnoses = None
#        """ Correlated diagnosies.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnoses`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedMedications = None
#        """ Correlated medications.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedMedications`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedProcedures = None
#        """ Correlated procedures.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedProcedures`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedPhenotypes = None
#        """ Correlated phenotypes.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedPhenotypes`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistribution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistribution, self).elementProperties()
        js.extend([
            ("units", "units", quantity.Quantity, False, None, True),
            ("min", "min", float, False, None, True),
            ("max", "max", float, False, None, True),
            ("mean", "mean", float, False, None, True),
            ("median", "median", float, False, None, True),
            ("stdDev", "stdDev", float, False, None, True),
            ("decile", "decile", ClinicalProfileLabScalarDistributionDecile, True, None, False),
            ("normalizedHigh", "normalizedHigh", float, False, None, False),
            ("normalizedLow", "normalizedLow", float, False, None, False),
            ("fractionAboveNormal", "fractionAboveNormal", float, False, None, False),
            ("fractionBelowNormal", "fractionBelowNormal", float, False, None, False),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionDecile(backboneelement.BackboneElement):
    """ Decile partitions.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionDecile"
    nth: int = None
    value: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.nth = None
#        """ Particular decile (10, 20, …).
#        Type `int`
#
#. """
#
#
#        self.value = None
#        """ Cutoff value for this decile.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionDecile, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionDecile, self).elementProperties()
        js.extend([
            ("nth", "nth", int, False, None, True),
            ("value", "value", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabs(backboneelement.BackboneElement):
    """ Correlated laboratory tests.
    
    An ordered list of the laboratory tests  that are most closely correlated.
    This list can be limited by the top "n" labs and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabs"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedLabsEntry]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.topn = None
#        """ Number of correlations cutoff (e.g. top 10).
#        Type `int`
#
#. """
#
#
#        self.abscorrelation = None
#        """ Minimum absolute value of correlation coefficient.
#        Type `float`
#
#. """
#
#
#        self.entry = None
#        """ Correlated lab.
#        List of `ClinicalProfileLabScalarDistributionCorrelatedLabsEntry` items
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedLabs, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabs, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedLabsEntry(backboneelement.BackboneElement):
    """ Correlated lab.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedLabsEntry"
    labcode: List[codeableconcept.CodeableConcept] = empty_list()
    coefficient: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.labcode = None
#        """ Lab code (LOINC) or Lab Group Code.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.coefficient = None
#        """ Correlation coefficient.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedLabsEntry, self).elementProperties()
        js.extend([
            ("labcode", "labcode", codeableconcept.CodeableConcept, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnoses(backboneelement.BackboneElement):
    """ Correlated diagnosies.
    
    An ordered list of  the diagnoses  that are most closely correlated.  This
    list can be limited by the top "n" diagnoses and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnoses"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.topn = None
#        """ Number of diagnoses cutoff (e.g. top 10).
#        Type `int`
#
#. """
#
#
#        self.abscorrelation = None
#        """ Minimum absolute value of correlation coefficient.
#        Type `float`
#
#. """
#
#
#        self.entry = None
#        """ Correlation entry.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry"
    code:codeableconcept.CodeableConcept = None
    coefficient: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Diagnosis code(s).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.coefficient = None
#        """ Correlation coefficient.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedDiagnosesEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedications(backboneelement.BackboneElement):
    """ Correlated medications.
    
    An ordered list of  the medications  that are most closely correlated.
    This list can be limited by the top "n" medications and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedications"
    topn: Optional[int] = None
    deviation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.topn = None
#        """ Number of medications cutoff (e.g. top 10).
#        Type `int`
#
#. """
#
#
#        self.deviation = None
#        """ Deviation cutoff.
#        Type `float`
#
#. """
#
#
#        self.entry = None
#        """ Correlation entry.
#        List of `ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry` items
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedMedications, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedMedications, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("deviation", "deviation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry"
    category: Optional[codeableconcept.CodeableConcept] = None
    labCodeableConcept:codeableconcept.CodeableConcept = None
    labReference:fhirreference.FHIRReference = None
    coefficient: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.category = None
#        """ Indicates the type of medication dispense (for example, where the
        medication is expected to be consumed or administered (i.e.
        inpatient or outpatient)).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.labCodeableConcept = None
#        """ Medication code(s).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.labReference = None
#        """ Medication code(s).
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.coefficient = None
#        """ Correlation coefficient.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedMedicationsEntry, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("labCodeableConcept", "labCodeableConcept", codeableconcept.CodeableConcept, False, "lab", True),
            ("labReference", "labReference", fhirreference.FHIRReference, False, "lab", True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProcedures(backboneelement.BackboneElement):
    """ Correlated procedures.
    
    An ordered list of  the procedures  that are most closely correlated.  This
    list can be limited by the top "n" procedures and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProcedures"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.topn = None
#        """ Number of rocedures cutoff (e.g. top 10).
#        Type `int`
#
#. """
#
#
#        self.abscorrelation = None
#        """ Minimum absolute value of correlation coefficient.
#        Type `float`
#
#. """
#
#
#        self.entry = None
#        """ Correlation entry.
#        List of `ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry` items
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedProcedures, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedProcedures, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry"
    code: List[codeableconcept.CodeableConcept] = empty_list()
    coefficient: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Procedure code(s).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.coefficient = None
#        """ Correlation coefficient.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedProceduresEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypes(backboneelement.BackboneElement):
    """ Correlated phenotypes.
    
    An ordered list of  the phenotypes  that are most closely correlated.  This
    list can be limited by the top "n" phenotypes and/or a cutoff on the
    absolute value of the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypes"
    topn: Optional[int] = None
    abscorrelation: Optional[float] = None
    entry: Optional[List[ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.topn = None
#        """ Number of phenotypes cutoff (e.g. top 10).
#        Type `int`
#
#. """
#
#
#        self.abscorrelation = None
#        """ Minimum absolute value of correlation coefficient.
#        Type `float`
#
#. """
#
#
#        self.entry = None
#        """ Correlation entry.
#        List of `ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry` items
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, self).elementProperties()
        js.extend([
            ("topn", "topn", int, False, None, False),
            ("abscorrelation", "abscorrelation", float, False, None, False),
            ("entry", "entry", ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry, True, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry(backboneelement.BackboneElement):
    """ Correlation entry.
    
    List of correlated phenotypes in descending order of the absolute value of
    the correlation coefficient.
    """
    resource_type: ClassVar[str] = "ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry"
    code:codeableconcept.CodeableConcept = None
    coefficient: float = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Phenotype codes.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.coefficient = None
#        """ Correlation coefficient.
#        Type `float`
#
#. """
#
        
#        super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileLabScalarDistributionCorrelatedPhenotypesEntry, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("coefficient", "coefficient", float, False, None, True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileMedication(backboneelement.BackboneElement):
    """ Medication profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedication"
    category: Optional[codeableconcept.CodeableConcept] = None
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    dosage: Optional[ClinicalProfileMedicationDosage] = None
    treatementDuration: Optional[float] = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.category = None
#        """ Indicates the type of medication dispense (for example, where the
        medication is expected to be consumed or administered (i.e.
        inpatient or outpatient)).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.medicationCodeableConcept = None
#        """ Medication(s) being profiled.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.medicationReference = None
#        """ Medication(s) being profiled.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.dosage = None
#        """ Details of how medication was taken.
#        Type `ClinicalProfileMedicationDosage`
#
# (represented as `dict` in JSON). """
#
#
#        self.treatementDuration = None
#        """ Duration of treatment (in 1 year).
#        Type `float`
#
#. """
#
#
#        self.frequencyPerYear = None
#        """ Frequency of treatments per patient per year.
#        Type `float`
#
#. """
#
#
#        self.fractionOfSubjects = None
#        """ Fraction of patients in cohort treated with this drug.
#        Type `float`
#
#. """
#
#
#        self.correlatedLabs = None
#        """ Correlated labs.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedDiagnoses = None
#        """ Correlated diagnosies.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnoses`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedMedications = None
#        """ Correlated medications.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedMedications`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedProcedures = None
#        """ Correlated procedures.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedProcedures`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedPhenotypes = None
#        """ Correlated phenotypes.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedPhenotypes`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileMedication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedication, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("dosage", "dosage", ClinicalProfileMedicationDosage, False, None, False),
            ("treatementDuration", "treatementDuration", float, False, None, False),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileMedicationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    """
    resource_type: ClassVar[str] = "ClinicalProfileMedicationDosage"
    text: Optional[str] = None
    site: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    route: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    method: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    dose: Optional[List[quantity.Quantity]] = empty_list()
    rateRatio: Optional[ratio.Ratio] = None
    rateQuantity: Optional[quantity.Quantity] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.text = None
#        """ Free text dosage instructions e.g. SIG.
#        Type `str`
#
#. """
#
#
#        self.site = None
#        """ Body site(s) administered to.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.route = None
#        """ Path(s) of substance into body.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.method = None
#        """ How the drug was administered.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.dose = None
#        """ Average amount of medication per dose.
#        List of `Quantity` items
#
# (represented as `dict` in JSON). """
#
#
#        self.rateRatio = None
#        """ Dose quantity per unit of time.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.rateQuantity = None
#        """ Dose quantity per unit of time.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileMedicationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileMedicationDosage, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, True, None, False),
            ("route", "route", codeableconcept.CodeableConcept, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, True, None, False),
            ("dose", "dose", quantity.Quantity, True, None, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileDiagnosis"
    code: List[codeableconcept.CodeableConcept] = empty_list()
    count: int = None
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ Diagnosis code(s).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.count = None
#        """ Number of times listed per patient per hear for each code.
#        Type `int`
#
#. """
#
#
#        self.frequencyPerYear = None
#        """ Frequency of this diagnosis per patient per year.
#        Type `float`
#
#. """
#
#
#        self.fractionOfSubjects = None
#        """ Fraction of patients in with this diagnosis.
#        Type `float`
#
#. """
#
#
#        self.correlatedLabs = None
#        """ Correlated labs.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedDiagnoses = None
#        """ Correlated diagnosies.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnoses`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedMedications = None
#        """ Correlated medications.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedMedications`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedProcedures = None
#        """ Correlated procedures.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedProcedures`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedPhenotypes = None
#        """ Correlated phenotypes.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedPhenotypes`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileDiagnosis, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("count", "count", int, False, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileProcedure(backboneelement.BackboneElement):
    """ Procedure profile entry.
    """
    resource_type: ClassVar[str] = "ClinicalProfileProcedure"
    code: List[codeableconcept.CodeableConcept] = empty_list()
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ ICD-10-PCS or CPT procedure code.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.frequencyPerYear = None
#        """ Frequency of procedure per patient per year.
#        Type `float`
#
#. """
#
#
#        self.fractionOfSubjects = None
#        """ Fraction of patients with this procedure per year.
#        Type `float`
#
#. """
#
#
#        self.correlatedLabs = None
#        """ Correlated labs.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedDiagnoses = None
#        """ Correlated diagnosies.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnoses`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedMedications = None
#        """ Correlated medications.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedMedications`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedProcedures = None
#        """ Correlated procedures.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedProcedures`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedPhenotypes = None
#        """ Correlated phenotypes.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedPhenotypes`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileProcedure, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio


@dataclass
class ClinicalProfileHpo(backboneelement.BackboneElement):
    """ HPO Profile Entry.
    
    Phenotypic description.
    """
    resource_type: ClassVar[str] = "ClinicalProfileHpo"
    code: List[codeableconcept.CodeableConcept] = empty_list()
    frequencyPerYear: Optional[float] = None
    fractionOfSubjects: float = None
    correlatedLabs: Optional[ClinicalProfileLabScalarDistributionCorrelatedLabs] = None
    correlatedDiagnoses: Optional[ClinicalProfileLabScalarDistributionCorrelatedDiagnoses] = None
    correlatedMedications: Optional[ClinicalProfileLabScalarDistributionCorrelatedMedications] = None
    correlatedProcedures: Optional[ClinicalProfileLabScalarDistributionCorrelatedProcedures] = None
    correlatedPhenotypes: Optional[ClinicalProfileLabScalarDistributionCorrelatedPhenotypes] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.code = None
#        """ HPO code.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.frequencyPerYear = None
#        """ Frequency of this code per patient per year.
#        Type `float`
#
#. """
#
#
#        self.fractionOfSubjects = None
#        """ Fraction of patients with this procedure per year.
#        Type `float`
#
#. """
#
#
#        self.correlatedLabs = None
#        """ Correlated labs.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedLabs`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedDiagnoses = None
#        """ Correlated diagnosies.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedDiagnoses`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedMedications = None
#        """ Correlated medications.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedMedications`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedProcedures = None
#        """ Correlated procedures.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedProcedures`
#
# (represented as `dict` in JSON). """
#
#
#        self.correlatedPhenotypes = None
#        """ Correlated phenotypes.
#        Type `ClinicalProfileLabScalarDistributionCorrelatedPhenotypes`
#
# (represented as `dict` in JSON). """
#
        
#        super(ClinicalProfileHpo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalProfileHpo, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, True),
            ("frequencyPerYear", "frequencyPerYear", float, False, None, False),
            ("fractionOfSubjects", "fractionOfSubjects", float, False, None, True),
            ("correlatedLabs", "correlatedLabs", ClinicalProfileLabScalarDistributionCorrelatedLabs, False, None, False),
            ("correlatedDiagnoses", "correlatedDiagnoses", ClinicalProfileLabScalarDistributionCorrelatedDiagnoses, False, None, False),
            ("correlatedMedications", "correlatedMedications", ClinicalProfileLabScalarDistributionCorrelatedMedications, False, None, False),
            ("correlatedProcedures", "correlatedProcedures", ClinicalProfileLabScalarDistributionCorrelatedProcedures, False, None, False),
            ("correlatedPhenotypes", "correlatedPhenotypes", ClinicalProfileLabScalarDistributionCorrelatedPhenotypes, False, None, False),
        ])
        return js
