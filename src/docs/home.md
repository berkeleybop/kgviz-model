# Introduction

A data model for describing configurations / stylesheets for visualzing graphs, and
in particular Knowledge Graphs or Ontologies. These graphs are characterized by features such as

 - having meaningful edge labels (subClassOf, partOf, developsFrom)
 - node IDs/URIs in addition to names/labels
 - node categories
 - additional rich metadata on the nodes or edges

An example of a use of this specification is [obographviz](https://github.com/cmungall/obographviz)

The main way in which this specification is intended to be used to to
specify stylesheets for graphical applications in the form of a JSON
document, so examples here are in JSON

These should conform to the JSON-Schema

However, other serializations are possible - e.g. RDF. See further on for details

## Examples

### Global styling

An example of a minimal JSON file instantiating a [StyleSheet](https://berkeleybop.github.io/kgviz-model/StyleSheet/) class:

```json
{
    "style": "filled",
    "fillcolor": "green"
}
```

This uses two properties:

 * [style](https://berkeleybop.github.io/kgviz-model/style/)
 * [fillcolor](https://berkeleybop.github.io/kgviz-model/fillcolor/)

Each of these properties are mapped to the URIs in the GraphViz documentation

These indicate that boxes should be filled and colored green

### Styling predicates (relations

[relationProperties](https://berkeleybop.github.io/kgviz-model/relationProperties/) maps a set of predicate CURIEs to edge properties:

```json
{
    "relationProperties": {
        "rdfs:subClassOf": {
            "color": "black",
            "penwith": 3,
            "arrowhead": "open",
            "label": ""
        },
        "BFO:0000050": {
            "arrowhead": "tee",
            "color": "blue"
        }
    }
}
```


## Graphviz vocabulary
