
# Class: PrefixConfiguration


style for a particular prefix (e.g. GO)

URI: [ex:PrefixConfiguration](https://w3id.org/kgviz/PrefixConfiguration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StyleSheet]++-%20prefixProperties%200..*>[PrefixConfiguration&#124;id:Node;fillcolor:Color%20%3F;penwidth:integer%20%3F;label:string%20%3F;color:Color%20%3F;fontcolor:Color%20%3F],[PrefixConfiguration]uses%20-.->[NodeProperty],[ElementConfiguration]^-[PrefixConfiguration],[StyleSheet],[NodeProperty],[ElementConfiguration])](https://yuml.me/diagram/nofunky;dir:TB/class/[StyleSheet]++-%20prefixProperties%200..*>[PrefixConfiguration&#124;id:Node;fillcolor:Color%20%3F;penwidth:integer%20%3F;label:string%20%3F;color:Color%20%3F;fontcolor:Color%20%3F],[PrefixConfiguration]uses%20-.->[NodeProperty],[ElementConfiguration]^-[PrefixConfiguration],[StyleSheet],[NodeProperty],[ElementConfiguration])

## Parents

 *  is_a: [ElementConfiguration](ElementConfiguration.md) - Abstract parent for all coniguration classes

## Uses Mixin

 *  mixin: [NodeProperty](NodeProperty.md)

## Referenced by Class

 *  **None** *[prefixProperties](prefixProperties.md)*  <sub>0..\*</sub>  **[PrefixConfiguration](PrefixConfiguration.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [Node](types/Node.md)
 * [fillcolor](fillcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

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

### Mixed in from NodeProperty:

 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)

### Mixed in from GeneralProperty:

 * [fontcolor](fontcolor.md)  <sub>0..1</sub>
     * Range: [Color](types/Color.md)
