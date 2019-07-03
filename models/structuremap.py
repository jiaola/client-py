#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import domainresource
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


from . import domainresource

@dataclass
class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    resource_type: ClassVar[str] = "StructureMap"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    group: List[ StructureMapGroup] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    import_fhir: Optional[List[str]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: str = None
    publisher: Optional[str] = None
    purpose: Optional[str] = None
    status: str = None
    structure: Optional[List[StructureMapStructure]] = empty_list()
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

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
#        self.contact = None
#        """ Contact details for the publisher.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.copyright = None
#        """ Use and/or publishing restrictions.
#        Type `str`
#
#. """
#
#
#        self.date = None
#        """ Date last changed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Natural language description of the structure map.
#        Type `str`
#
#. """
#
#
#        self.experimental = None
#        """ For testing purposes, not real usage.
#        Type `bool`
#
#. """
#
#
#        self.group = None
#        """ Named sections for reader convenience.
#        List of `StructureMapGroup` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Additional identifier for the structure map.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.import_fhir = None
#        """ Other maps used by this map (canonical URLs).
#        List of `str` items
#
#. """
#
#
#        self.jurisdiction = None
#        """ Intended jurisdiction for structure map (if applicable).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Name for this structure map (computer friendly).
#        Type `str`
#
#. """
#
#
#        self.publisher = None
#        """ Name of the publisher (organization or individual).
#        Type `str`
#
#. """
#
#
#        self.purpose = None
#        """ Why this structure map is defined.
#        Type `str`
#
#. """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.structure = None
#        """ Structure Definition used by this map.
#        List of `StructureMapStructure` items
#
# (represented as `dict` in JSON). """
#
#
#        self.title = None
#        """ Name for this structure map (human friendly).
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical identifier for this structure map, represented as a URI
        (globally unique).
#        Type `str`
#
#. """
#
#
#        self.useContext = None
#        """ The context that the content is intended to support.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#
#
#        self.version = None
#        """ Business version of the structure map.
#        Type `str`
#
#. """
#

#        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("copyright", "copyright", str, {  # #}False, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("experimental", "experimental", bool, {  # #}False, None, {  # #}False),
            ("group", "group", StructureMapGroup, {  # #}True, None, {  # #}True),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("import_fhir", "import", str, {  # #}True, None, {  # #}False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("purpose", "purpose", str, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("structure", "structure", StructureMapStructure, {  # #}True, None, {  # #}False),
            ("title", "title", str, {  # #}False, None, {  # #}False),
            ("url", "url", str, {  # #}False, None, {  # #}True),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


from . import backboneelement

@dataclass
class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.

    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    resource_type: ClassVar[str] = "StructureMapGroup"
    documentation: Optional[str] = None
    extends: Optional[str] = None
    input: List[ StructureMapGroupInput] = empty_list()
    name: str = None
    rule: List[ StructureMapGroupRule] = empty_list()
    typeMode: str = None

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
#        self.documentation = None
#        """ Additional description/explanation for group.
#        Type `str`
#
#. """
#
#
#        self.extends = None
#        """ Another group that this group adds rules to.
#        Type `str`
#
#. """
#
#
#        self.input = None
#        """ Named instance provided when invoking the map.
#        List of `StructureMapGroupInput` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Human-readable label.
#        Type `str`
#
#. """
#
#
#        self.rule = None
#        """ Transform Rule from source to target.
#        List of `StructureMapGroupRule` items
#
# (represented as `dict` in JSON). """
#
#
#        self.typeMode = None
#        """ none | types | type-and-types.
#        Type `str`
#
#. """
#

#        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("extends", "extends", str, {  # #}False, None, {  # #}False),
            ("input", "input", StructureMapGroupInput, {  # #}True, None, {  # #}True),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("rule", "rule", StructureMapGroupRule, {  # #}True, None, {  # #}True),
            ("typeMode", "typeMode", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.

    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    resource_type: ClassVar[str] = "StructureMapGroupInput"
    documentation: Optional[str] = None
    mode: str = None
    name: str = None
    type: Optional[str] = None

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
#        self.documentation = None
#        """ Documentation for this instance of data.
#        Type `str`
#
#. """
#
#
#        self.mode = None
#        """ source | target.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name for this instance of data.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ Type for this instance of data.
#        Type `str`
#
#. """
#

#        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("type", "type", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRule"
    dependent: Optional[List[StructureMapGroupRuleDependent]] = empty_list()
    documentation: Optional[str] = None
    name: str = None
    rule: Optional[List[StructureMapGroupRule]] = empty_list()
    source: List[ StructureMapGroupRuleSource] = empty_list()
    target: Optional[List[StructureMapGroupRuleTarget]] = empty_list()

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
#        self.dependent = None
#        """ Which other rules to apply in the context of this rule.
#        List of `StructureMapGroupRuleDependent` items
#
# (represented as `dict` in JSON). """
#
#
#        self.documentation = None
#        """ Documentation for this instance of data.
#        Type `str`
#
#. """
#
#
#        self.name = None
#        """ Name of the rule for internal references.
#        Type `str`
#
#. """
#
#
#        self.rule = None
#        """ Rules contained in this rule.
#        List of `StructureMapGroupRule` items
#
# (represented as `dict` in JSON). """
#
#
#        self.source = None
#        """ Source inputs to the mapping.
#        List of `StructureMapGroupRuleSource` items
#
# (represented as `dict` in JSON). """
#
#
#        self.target = None
#        """ Content to create because of this mapping rule.
#        List of `StructureMapGroupRuleTarget` items
#
# (represented as `dict` in JSON). """
#

#        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, {  # #}True, None, {  # #}False),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("rule", "rule", StructureMapGroupRule, {  # #}True, None, {  # #}False),
            ("source", "source", StructureMapGroupRuleSource, {  # #}True, None, {  # #}True),
            ("target", "target", StructureMapGroupRuleTarget, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleDependent"
    name: str = None
    variable: List[ str] = empty_list()

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
#        self.name = None
#        """ Name of a rule or group to apply.
#        Type `str`
#
#. """
#
#
#        self.variable = None
#        """ Variable to pass to the rule or group.
#        List of `str` items
#
#. """
#

#        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("variable", "variable", str, {  # #}True, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleSource"
    check: Optional[str] = None
    condition: Optional[str] = None
    context: str = None
    defaultValueAddress: Optional[address.Address] = None
    defaultValueAge: Optional[age.Age] = None
    defaultValueAnnotation: Optional[annotation.Annotation] = None
    defaultValueAttachment: Optional[attachment.Attachment] = None
    defaultValueBase64Binary: Optional[str] = None
    defaultValueBoolean: Optional[bool] = None
    defaultValueCanonical: Optional[str] = None
    defaultValueCode: Optional[str] = None
    defaultValueCodeableConcept: Optional[codeableconcept.CodeableConcept] = None
    defaultValueCoding: Optional[coding.Coding] = None
    defaultValueContactDetail: Optional[contactdetail.ContactDetail] = None
    defaultValueContactPoint: Optional[contactpoint.ContactPoint] = None
    defaultValueContributor: Optional[contributor.Contributor] = None
    defaultValueCount: Optional[count.Count] = None
    defaultValueDataRequirement: Optional[datarequirement.DataRequirement] = None
    defaultValueDate: Optional[fhirdate.FHIRDate] = None
    defaultValueDateTime: Optional[fhirdate.FHIRDate] = None
    defaultValueDecimal: Optional[float] = None
    defaultValueDistance: Optional[distance.Distance] = None
    defaultValueDosage: Optional[dosage.Dosage] = None
    defaultValueDuration: Optional[duration.Duration] = None
    defaultValueExpression: Optional[expression.Expression] = None
    defaultValueHumanName: Optional[humanname.HumanName] = None
    defaultValueId: Optional[str] = None
    defaultValueIdentifier: Optional[identifier.Identifier] = None
    defaultValueInstant: Optional[fhirdate.FHIRDate] = None
    defaultValueInteger: Optional[int] = None
    defaultValueMarkdown: Optional[str] = None
    defaultValueMoney: Optional[money.Money] = None
    defaultValueOid: Optional[str] = None
    defaultValueParameterDefinition: Optional[parameterdefinition.ParameterDefinition] = None
    defaultValuePeriod: Optional[period.Period] = None
    defaultValuePositiveInt: Optional[int] = None
    defaultValueQuantity: Optional[quantity.Quantity] = None
    defaultValueRange: Optional[range.Range] = None
    defaultValueRatio: Optional[ratio.Ratio] = None
    defaultValueReference: Optional[fhirreference.FHIRReference] = None
    defaultValueRelatedArtifact: Optional[relatedartifact.RelatedArtifact] = None
    defaultValueSampledData: Optional[sampleddata.SampledData] = None
    defaultValueSignature: Optional[signature.Signature] = None
    defaultValueString: Optional[str] = None
    defaultValueTime: Optional[fhirdate.FHIRDate] = None
    defaultValueTiming: Optional[timing.Timing] = None
    defaultValueTriggerDefinition: Optional[triggerdefinition.TriggerDefinition] = None
    defaultValueUnsignedInt: Optional[int] = None
    defaultValueUri: Optional[str] = None
    defaultValueUrl: Optional[str] = None
    defaultValueUsageContext: Optional[usagecontext.UsageContext] = None
    defaultValueUuid: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[str] = None
    logMessage: Optional[str] = None
    max: Optional[str] = None
    min: Optional[int] = None
    type: Optional[str] = None
    variable: Optional[str] = None

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
#        self.check = None
#        """ FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.
#        Type `str`
#
#. """
#
#
#        self.condition = None
#        """ FHIRPath expression  - must be true or the rule does not apply.
#        Type `str`
#
#. """
#
#
#        self.context = None
#        """ Type or variable this rule applies to.
#        Type `str`
#
#. """
#
#
#        self.defaultValueAddress = None
#        """ Default value if no value exists.
#        Type `Address`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueAge = None
#        """ Default value if no value exists.
#        Type `Age`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueAnnotation = None
#        """ Default value if no value exists.
#        Type `Annotation`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueAttachment = None
#        """ Default value if no value exists.
#        Type `Attachment`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueBase64Binary = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueBoolean = None
#        """ Default value if no value exists.
#        Type `bool`
#
#. """
#
#
#        self.defaultValueCanonical = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueCode = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueCodeableConcept = None
#        """ Default value if no value exists.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueCoding = None
#        """ Default value if no value exists.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueContactDetail = None
#        """ Default value if no value exists.
#        Type `ContactDetail`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueContactPoint = None
#        """ Default value if no value exists.
#        Type `ContactPoint`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueContributor = None
#        """ Default value if no value exists.
#        Type `Contributor`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueCount = None
#        """ Default value if no value exists.
#        Type `Count`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueDataRequirement = None
#        """ Default value if no value exists.
#        Type `DataRequirement`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueDate = None
#        """ Default value if no value exists.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.defaultValueDateTime = None
#        """ Default value if no value exists.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.defaultValueDecimal = None
#        """ Default value if no value exists.
#        Type `float`
#
#. """
#
#
#        self.defaultValueDistance = None
#        """ Default value if no value exists.
#        Type `Distance`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueDosage = None
#        """ Default value if no value exists.
#        Type `Dosage`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueDuration = None
#        """ Default value if no value exists.
#        Type `Duration`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueExpression = None
#        """ Default value if no value exists.
#        Type `Expression`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueHumanName = None
#        """ Default value if no value exists.
#        Type `HumanName`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueId = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueIdentifier = None
#        """ Default value if no value exists.
#        Type `Identifier`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueInstant = None
#        """ Default value if no value exists.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.defaultValueInteger = None
#        """ Default value if no value exists.
#        Type `int`
#
#. """
#
#
#        self.defaultValueMarkdown = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueMoney = None
#        """ Default value if no value exists.
#        Type `Money`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueOid = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueParameterDefinition = None
#        """ Default value if no value exists.
#        Type `ParameterDefinition`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValuePeriod = None
#        """ Default value if no value exists.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValuePositiveInt = None
#        """ Default value if no value exists.
#        Type `int`
#
#. """
#
#
#        self.defaultValueQuantity = None
#        """ Default value if no value exists.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueRange = None
#        """ Default value if no value exists.
#        Type `Range`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueRatio = None
#        """ Default value if no value exists.
#        Type `Ratio`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueReference = None
#        """ Default value if no value exists.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueRelatedArtifact = None
#        """ Default value if no value exists.
#        Type `RelatedArtifact`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueSampledData = None
#        """ Default value if no value exists.
#        Type `SampledData`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueSignature = None
#        """ Default value if no value exists.
#        Type `Signature`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueString = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueTime = None
#        """ Default value if no value exists.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.defaultValueTiming = None
#        """ Default value if no value exists.
#        Type `Timing`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueTriggerDefinition = None
#        """ Default value if no value exists.
#        Type `TriggerDefinition`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueUnsignedInt = None
#        """ Default value if no value exists.
#        Type `int`
#
#. """
#
#
#        self.defaultValueUri = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueUrl = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.defaultValueUsageContext = None
#        """ Default value if no value exists.
#        Type `UsageContext`
#
# (represented as `dict` in JSON). """
#
#
#        self.defaultValueUuid = None
#        """ Default value if no value exists.
#        Type `str`
#
#. """
#
#
#        self.element = None
#        """ Optional field for this source.
#        Type `str`
#
#. """
#
#
#        self.listMode = None
#        """ first | not_first | last | not_last | only_one.
#        Type `str`
#
#. """
#
#
#        self.logMessage = None
#        """ Message to put in log if source exists (FHIRPath).
#        Type `str`
#
#. """
#
#
#        self.max = None
#        """ Specified maximum cardinality (number or *).
#        Type `str`
#
#. """
#
#
#        self.min = None
#        """ Specified minimum cardinality.
#        Type `int`
#
#. """
#
#
#        self.type = None
#        """ Rule only applies if source has this type.
#        Type `str`
#
#. """
#
#
#        self.variable = None
#        """ Named context for field, if a field is specified.
#        Type `str`
#
#. """
#

#        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, {  # #}False, None, {  # #}False),
            ("condition", "condition", str, {  # #}False, None, {  # #}False),
            ("context", "context", str, {  # #}False, None, {  # #}True),
            ("defaultValueAddress", "defaultValueAddress", address.Address, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueAge", "defaultValueAge", age.Age, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueCanonical", "defaultValueCanonical", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueCode", "defaultValueCode", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueCount", "defaultValueCount", count.Count, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDecimal", "defaultValueDecimal", float, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueId", "defaultValueId", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueInteger", "defaultValueInteger", int, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueOid", "defaultValueOid", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueRange", "defaultValueRange", range.Range, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueString", "defaultValueString", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueUri", "defaultValueUri", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueUrl", "defaultValueUrl", str, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, {  # #}False, "defaultValue", {  # #}False),
            ("defaultValueUuid", "defaultValueUuid", str, {  # #}False, "defaultValue", {  # #}False),
            ("element", "element", str, {  # #}False, None, {  # #}False),
            ("listMode", "listMode", str, {  # #}False, None, {  # #}False),
            ("logMessage", "logMessage", str, {  # #}False, None, {  # #}False),
            ("max", "max", str, {  # #}False, None, {  # #}False),
            ("min", "min", int, {  # #}False, None, {  # #}False),
            ("type", "type", str, {  # #}False, None, {  # #}False),
            ("variable", "variable", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTarget"
    context: Optional[str] = None
    contextType: Optional[str] = None
    element: Optional[str] = None
    listMode: Optional[List[str]] = empty_list()
    listRuleId: Optional[str] = None
    parameter: Optional[List[StructureMapGroupRuleTargetParameter]] = empty_list()
    transform: Optional[str] = None
    variable: Optional[str] = None

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
#        self.context = None
#        """ Type or variable this rule applies to.
#        Type `str`
#
#. """
#
#
#        self.contextType = None
#        """ type | variable.
#        Type `str`
#
#. """
#
#
#        self.element = None
#        """ Field to create in the context.
#        Type `str`
#
#. """
#
#
#        self.listMode = None
#        """ first | share | last | collate.
#        List of `str` items
#
#. """
#
#
#        self.listRuleId = None
#        """ Internal rule reference for shared list items.
#        Type `str`
#
#. """
#
#
#        self.parameter = None
#        """ Parameters to the transform.
#        List of `StructureMapGroupRuleTargetParameter` items
#
# (represented as `dict` in JSON). """
#
#
#        self.transform = None
#        """ create | copy +.
#        Type `str`
#
#. """
#
#
#        self.variable = None
#        """ Named context for field, if desired, and a field is specified.
#        Type `str`
#
#. """
#

#        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, {  # #}False, None, {  # #}False),
            ("contextType", "contextType", str, {  # #}False, None, {  # #}False),
            ("element", "element", str, {  # #}False, None, {  # #}False),
            ("listMode", "listMode", str, {  # #}True, None, {  # #}False),
            ("listRuleId", "listRuleId", str, {  # #}False, None, {  # #}False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, {  # #}True, None, {  # #}False),
            ("transform", "transform", str, {  # #}False, None, {  # #}False),
            ("variable", "variable", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """
    resource_type: ClassVar[str] = "StructureMapGroupRuleTargetParameter"
    valueBoolean: bool = None
    valueDecimal: float = None
    valueId: str = None
    valueInteger: int = None
    valueString: str = None

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
#        self.valueBoolean = None
#        """ Parameter value - variable or literal.
#        Type `bool`
#
#. """
#
#
#        self.valueDecimal = None
#        """ Parameter value - variable or literal.
#        Type `float`
#
#. """
#
#
#        self.valueId = None
#        """ Parameter value - variable or literal.
#        Type `str`
#
#. """
#
#
#        self.valueInteger = None
#        """ Parameter value - variable or literal.
#        Type `int`
#
#. """
#
#
#        self.valueString = None
#        """ Parameter value - variable or literal.
#        Type `str`
#
#. """
#

#        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, {  # #}False, "value", {  # #}True),
            ("valueDecimal", "valueDecimal", float, {  # #}False, "value", {  # #}True),
            ("valueId", "valueId", str, {  # #}False, "value", {  # #}True),
            ("valueInteger", "valueInteger", int, {  # #}False, "value", {  # #}True),
            ("valueString", "valueString", str, {  # #}False, "value", {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext


@dataclass
class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.

    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    resource_type: ClassVar[str] = "StructureMapStructure"
    alias: Optional[str] = None
    documentation: Optional[str] = None
    mode: str = None
    url: str = None

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
#        self.alias = None
#        """ Name for type in this map.
#        Type `str`
#
#. """
#
#
#        self.documentation = None
#        """ Documentation on use of structure.
#        Type `str`
#
#. """
#
#
#        self.mode = None
#        """ source | queried | target | produced.
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical reference to structure definition.
#        Type `str`
#
#. """
#

#        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, {  # #}False, None, {  # #}False),
            ("documentation", "documentation", str, {  # #}False, None, {  # #}False),
            ("mode", "mode", str, {  # #}False, None, {  # #}True),
            ("url", "url", str, {  # #}False, None, {  # #}True),
        ])
        return js