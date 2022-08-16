# Auto generated from graphviz.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-25 08:37
# Schema: GraphViz
#
# id: https://w3id.org/kgviz/graphviz
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GV = CurieNamespace('gv', 'https://w3id.org/kgviz/graphviz')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GV


# Types
class Color(str):
    """ e.g. red, green """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "Color"
    type_model_uri = GV.Color


# Class references



class GraphvizAspect(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.GraphvizAspect
    class_class_curie: ClassVar[str] = "gv:GraphvizAspect"
    class_name: ClassVar[str] = "graphviz aspect"
    class_model_uri: ClassVar[URIRef] = GV.GraphvizAspect


class EdgeAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.EdgeAspect
    class_class_curie: ClassVar[str] = "gv:EdgeAspect"
    class_name: ClassVar[str] = "edge aspect"
    class_model_uri: ClassVar[URIRef] = GV.EdgeAspect


class NodeAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.NodeAspect
    class_class_curie: ClassVar[str] = "gv:NodeAspect"
    class_name: ClassVar[str] = "node aspect"
    class_model_uri: ClassVar[URIRef] = GV.NodeAspect


class RootGraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.RootGraphAspect
    class_class_curie: ClassVar[str] = "gv:RootGraphAspect"
    class_name: ClassVar[str] = "root graph aspect"
    class_model_uri: ClassVar[URIRef] = GV.RootGraphAspect


class SubgraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.SubgraphAspect
    class_class_curie: ClassVar[str] = "gv:SubgraphAspect"
    class_name: ClassVar[str] = "subgraph aspect"
    class_model_uri: ClassVar[URIRef] = GV.SubgraphAspect


class ClusterSubgraphAspect(GraphvizAspect):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GV.ClusterSubgraphAspect
    class_class_curie: ClassVar[str] = "gv:ClusterSubgraphAspect"
    class_name: ClassVar[str] = "cluster subgraph aspect"
    class_model_uri: ClassVar[URIRef] = GV.ClusterSubgraphAspect


# Enumerations
class StyleType(EnumDefinitionImpl):

    dashed = PermissibleValue(text="dashed")
    dotted = PermissibleValue(text="dotted")
    solid = PermissibleValue(text="solid")
    invis = PermissibleValue(text="invis")
    bold = PermissibleValue(text="bold")
    tapered = PermissibleValue(text="tapered")
    filled = PermissibleValue(text="filled")
    striped = PermissibleValue(text="striped")
    wedged = PermissibleValue(text="wedged")
    diagonals = PermissibleValue(text="diagonals")
    rounded = PermissibleValue(text="rounded")

    _defn = EnumDefinition(
        name="StyleType",
    )

class ArrowType(EnumDefinitionImpl):

    normal = PermissibleValue(text="normal")
    inv = PermissibleValue(text="inv")
    dot = PermissibleValue(text="dot")
    invdot = PermissibleValue(text="invdot")
    odot = PermissibleValue(text="odot")
    invodot = PermissibleValue(text="invodot")
    none = PermissibleValue(text="none")
    tee = PermissibleValue(text="tee")
    empty = PermissibleValue(text="empty")
    invempty = PermissibleValue(text="invempty")
    diamond = PermissibleValue(text="diamond")
    odiamond = PermissibleValue(text="odiamond")
    ediamond = PermissibleValue(text="ediamond")
    crow = PermissibleValue(text="crow")
    box = PermissibleValue(text="box")
    obox = PermissibleValue(text="obox")
    open = PermissibleValue(text="open")
    halfopen = PermissibleValue(text="halfopen")
    vee = PermissibleValue(text="vee")

    _defn = EnumDefinition(
        name="ArrowType",
    )

# Slots

