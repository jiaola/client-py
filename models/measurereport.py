#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2019-07-03.
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
from . import period
from . import quantity


from . import domainresource

@dataclass
class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.

    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    resource_type: ClassVar[str] = "MeasureReport"
    date: Optional[fhirdate.FHIRDate] = None
    evaluatedResource: Optional[List[fhirreference.FHIRReference]] = empty_list()
    group: Optional[List[MeasureReportGroup]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    improvementNotation: Optional[codeableconcept.CodeableConcept] = None
    measure: str = None
    period:period.Period = None
    reporter: Optional[fhirreference.FHIRReference] = None
    status: str = None
    subject: Optional[fhirreference.FHIRReference] = None
    type: str = None

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
#        self.date = None
#        """ When the report was generated.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.evaluatedResource = None
#        """ What data was used to calculate the measure score.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.group = None
#        """ Measure results for each group.
#        List of `MeasureReportGroup` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Additional identifier for the MeasureReport.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.improvementNotation = None
#        """ increase | decrease.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.measure = None
#        """ What measure was calculated.
#        Type `str`
#
#. """
#
#
#        self.period = None
#        """ What period the report covers.
#        Type `Period`
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
#        self.status = None
#        """ complete | pending | error.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ What individual(s) the report is for.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ individual | subject-list | summary | data-collection.
#        Type `str`
#
#. """
#

#        super(MeasureReport, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("evaluatedResource", "evaluatedResource", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("group", "group", MeasureReportGroup, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("measure", "measure", str, {  # #}False, None, {  # #}True),
            ("period", "period", period.Period, {  # #}False, None, {  # #}True),
            ("reporter", "reporter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}True),
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
from . import period
from . import quantity


from . import backboneelement

@dataclass
class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.

    The results of the calculation, one for each population group in the
    measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroup"
    code: Optional[codeableconcept.CodeableConcept] = None
    measureScore: Optional[quantity.Quantity] = None
    population: Optional[List[MeasureReportGroupPopulation]] = empty_list()
    stratifier: Optional[List[MeasureReportGroupStratifier]] = empty_list()

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
#        """ Meaning of the group.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.measureScore = None
#        """ What score this group achieved.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.population = None
#        """ The populations in the group.
#        List of `MeasureReportGroupPopulation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.stratifier = None
#        """ Stratification results.
#        List of `MeasureReportGroupStratifier` items
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("measureScore", "measureScore", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("population", "population", MeasureReportGroupPopulation, {  # #}True, None, {  # #}False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, {  # #}True, None, {  # #}False),
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
from . import period
from . import quantity


@dataclass
class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.

    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupPopulation"
    code: Optional[codeableconcept.CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[fhirreference.FHIRReference] = None

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
#        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.count = None
#        """ Size of the population.
#        Type `int`
#
#. """
#
#
#        self.subjectResults = None
#        """ For subject-list reports, the subject results in this population.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("count", "count", int, {  # #}False, None, {  # #}False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
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
from . import period
from . import quantity


@dataclass
class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.

    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifier"
    code: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    stratum: Optional[List[MeasureReportGroupStratifierStratum]] = empty_list()

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
#        """ What stratifier of the group.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.stratum = None
#        """ Stratum results, one for each unique value, or set of values, in
        the stratifier, or stratifier components.
#        List of `MeasureReportGroupStratifierStratum` items
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, {  # #}True, None, {  # #}False),
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
from . import period
from . import quantity


@dataclass
class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.

    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratum"
    component: Optional[List[MeasureReportGroupStratifierStratumComponent]] = empty_list()
    measureScore: Optional[quantity.Quantity] = None
    population: Optional[List[MeasureReportGroupStratifierStratumPopulation]] = empty_list()
    value: Optional[codeableconcept.CodeableConcept] = None

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
#        self.component = None
#        """ Stratifier component values.
#        List of `MeasureReportGroupStratifierStratumComponent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.measureScore = None
#        """ What score this stratum achieved.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.population = None
#        """ Population results in this stratum.
#        List of `MeasureReportGroupStratifierStratumPopulation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.value = None
#        """ The stratum value, e.g. male.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroupStratifierStratum, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("component", "component", MeasureReportGroupStratifierStratumComponent, {  # #}True, None, {  # #}False),
            ("measureScore", "measureScore", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, {  # #}True, None, {  # #}False),
            ("value", "value", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
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
from . import period
from . import quantity


@dataclass
class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ Stratifier component values.

    A stratifier component value.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumComponent"
    code:codeableconcept.CodeableConcept = None
    value:codeableconcept.CodeableConcept = None

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
#        """ What stratifier component of the group.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.value = None
#        """ The stratum component value, e.g. male.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroupStratifierStratumComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("value", "value", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
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
from . import period
from . import quantity


@dataclass
class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.

    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    resource_type: ClassVar[str] = "MeasureReportGroupStratifierStratumPopulation"
    code: Optional[codeableconcept.CodeableConcept] = None
    count: Optional[int] = None
    subjectResults: Optional[fhirreference.FHIRReference] = None

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
#        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.count = None
#        """ Size of the population.
#        Type `int`
#
#. """
#
#
#        self.subjectResults = None
#        """ For subject-list reports, the subject results in this population.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(MeasureReportGroupStratifierStratumPopulation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("count", "count", int, {  # #}False, None, {  # #}False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
        ])
        return js