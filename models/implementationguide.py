#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2019-07-15.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import usagecontext

from . import domainresource

@dataclass
class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    resource_type: ClassVar[str] = "ImplementationGuide"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[fhirdate.FHIRDate] = None
    definition: Optional[ImplementationGuideDefinition] = None
    dependsOn: Optional[List[ImplementationGuideDependsOn]] = empty_list()
    description: Optional[str] = None
    experimental: Optional[bool] = None
    fhirVersion: List[ str] = empty_list()
    global_fhir: Optional[List[ImplementationGuideGlobal]] = empty_list()
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    license: Optional[str] = None
    manifest: Optional[ImplementationGuideManifest] = None
    name: str = None
    packageId: str = None
    publisher: Optional[str] = None
    status: str = None
    title: Optional[str] = None
    url: str = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", ImplementationGuideDefinition, False, None, False),
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, True),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("license", "license", str, False, None, False),
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False),
            ("name", "name", str, False, None, True),
            ("packageId", "packageId", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js

from . import backboneelement

@dataclass
class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.

    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinition"
    grouping: Optional[List[ImplementationGuideDefinitionGrouping]] = empty_list()
    page: Optional[ImplementationGuideDefinitionPage] = None
    parameter: Optional[List[ImplementationGuideDefinitionParameter]] = empty_list()
    resource: List[ ImplementationGuideDefinitionResource] = empty_list()
    template: Optional[List[ImplementationGuideDefinitionTemplate]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False),
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False),
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False),
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True),
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False),
        ])
        return js

@dataclass
class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.

    A logical group of resources. Logical groups can be used when building
    pages.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionGrouping"
    description: Optional[str] = None
    name: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionPage"
    generation: str = None
    nameReference:fhirreference.FHIRReference = None
    nameUrl: str = None
    page: Optional[List[ImplementationGuideDefinitionPage]] = empty_list()
    title: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("generation", "generation", str, False, None, True),
            ("nameReference", "nameReference", fhirreference.FHIRReference, False, "name", True),
            ("nameUrl", "nameUrl", str, False, "name", True),
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionParameter"
    code: str = None
    value: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionResource"
    description: Optional[str] = None
    exampleBoolean: Optional[bool] = None
    exampleCanonical: Optional[str] = None
    fhirVersion: Optional[List[str]] = empty_list()
    groupingId: Optional[str] = None
    name: Optional[str] = None
    reference:fhirreference.FHIRReference = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("fhirVersion", "fhirVersion", str, True, None, False),
            ("groupingId", "groupingId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDefinitionTemplate"
    code: str = None
    scope: Optional[str] = None
    source: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("scope", "scope", str, False, None, False),
            ("source", "source", str, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    resource_type: ClassVar[str] = "ImplementationGuideDependsOn"
    packageId: Optional[str] = None
    uri: str = None
    version: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("packageId", "packageId", str, False, None, False),
            ("uri", "uri", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js

@dataclass
class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    resource_type: ClassVar[str] = "ImplementationGuideGlobal"
    profile: str = None
    type: str = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js

@dataclass
class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.

    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifest"
    image: Optional[List[str]] = empty_list()
    other: Optional[List[str]] = empty_list()
    page: Optional[List[ImplementationGuideManifestPage]] = empty_list()
    rendering: Optional[str] = None
    resource: List[ ImplementationGuideManifestResource] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("image", "image", str, True, None, False),
            ("other", "other", str, True, None, False),
            ("page", "page", ImplementationGuideManifestPage, True, None, False),
            ("rendering", "rendering", str, False, None, False),
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True),
        ])
        return js

@dataclass
class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.

    Information about a page within the IG.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestPage"
    anchor: Optional[List[str]] = empty_list()
    name: str = None
    title: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("anchor", "anchor", str, True, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
        ])
        return js

@dataclass
class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    resource_type: ClassVar[str] = "ImplementationGuideManifestResource"
    exampleBoolean: Optional[bool] = None
    exampleCanonical: Optional[str] = None
    reference:fhirreference.FHIRReference = None
    relativePath: Optional[str] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    #def __post_init__(self, jsondict, strict) -> None:
    #    fhirabstractbase.FHIRAbstractBase(jsondict, strict)

    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("relativePath", "relativePath", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']