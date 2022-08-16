
# Class: AnyConfiguration


Generic configuration that inherits all aspects of both node and edge configurations

URI: [kgviz:AnyConfiguration](https://w3id.org/kgviz/AnyConfiguration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeProperty],[ElementConfiguration],[EdgeProperty],[ConditionalProperty]++-%20properties%200..1>[AnyConfiguration&#124;penwidth:integer%20%3F;label:string%20%3F;color:Color%20%3F;fontcolor:Color%20%3F;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F],[AnyConfiguration]uses%20-.->[NodeProperty],[AnyConfiguration]uses%20-.->[EdgeProperty],[ElementConfiguration]^-[AnyConfiguration],[ConditionalProperty])](https://yuml.me/diagram/nofunky;dir:TB/class/[NodeProperty],[ElementConfiguration],[EdgeProperty],[ConditionalProperty]++-%20properties%200..1>[AnyConfiguration&#124;penwidth:integer%20%3F;label:string%20%3F;color:Color%20%3F;fontcolor:Color%20%3F;arrowhead:ArrowType%20%3F;arrowtail:ArrowType%20%3F],[AnyConfiguration]uses%20-.->[NodeProperty],[AnyConfiguration]uses%20-.->[EdgeProperty],[ElementConfiguration]^-[AnyConfiguration],[ConditionalProperty])

## Parents

 *  is_a: [ElementConfiguration](ElementConfiguration.md) - Abstract parent for all coniguration classes

## Uses Mixin

 *  mixin: [NodeProperty](NodeProperty.md)
 *  mixin: [EdgeProperty](EdgeProperty.md) - a property object for an edge/relation

## Referenced by Class

 *  **None** *[properties](properties.md)*  <sub>0..1</sub>  **[AnyConfiguration](AnyConfiguration.md)**

## Attributes


### Mixed in from GeneralProperty:

 * [penwidth](penwidth.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)

### Mixed in from GeneralProperty:

 * [label](label.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Mixed in from NodeProperty:

 * [color](color.md)  <sub>0..1</sub>
     * Description: Basic drawing color for graphics, not text. For the latter, use the fontcolor attribute.
     * Range: [Color](types/Color.md)

### Mixed in from GeneralProperty:

 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

### Mixed in from NodeProperty:

 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

### Mixed in from EdgeProperty:

 * [arrowhead](arrowhead.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)

### Mixed in from EdgeProperty:

 * [arrowtail](arrowtail.md)  <sub>0..1</sub>
     * Range: [ArrowType](ArrowType.md)
