

CREATE TABLE "AnyConfiguration" (
	penwidth INTEGER, 
	label TEXT, 
	color TEXT, 
	fontcolor TEXT, 
	arrowhead VARCHAR(8), 
	arrowtail VARCHAR(8), 
	PRIMARY KEY (penwidth, label, color, fontcolor, arrowhead, arrowtail)
);

CREATE TABLE "Condition" (
	type TEXT, 
	subset TEXT, 
	PRIMARY KEY (type, subset)
);

CREATE TABLE "ConditionalProperty" (
	fillcolor TEXT, 
	conditions TEXT, 
	properties TEXT, 
	PRIMARY KEY (fillcolor, conditions, properties)
);

CREATE TABLE "PrefixConfiguration" (
	id TEXT NOT NULL, 
	fillcolor TEXT, 
	penwidth INTEGER, 
	label TEXT, 
	color TEXT, 
	fontcolor TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "RelationConfiguration" (
	id TEXT NOT NULL, 
	color TEXT, 
	penwidth INTEGER, 
	label TEXT, 
	fontcolor TEXT, 
	arrowhead VARCHAR(8), 
	arrowtail VARCHAR(8), 
	PRIMARY KEY (id)
);

CREATE TABLE "StyleSheet" (
	style VARCHAR(9), 
	styles VARCHAR(9), 
	fillcolor TEXT, 
	"labelFrom" TEXT, 
	"highlightIds" TEXT, 
	"displayAnnotations" TEXT, 
	"cliqueRelations" TEXT, 
	"containmentRelations" TEXT, 
	reasoning VARCHAR(20), 
	"excludeSingletons" BOOLEAN, 
	"relationProperties" TEXT, 
	"prefixProperties" TEXT, 
	"conditionalProperties" TEXT, 
	"nodeFilter" TEXT, 
	PRIMARY KEY (style, styles, fillcolor, "labelFrom", "highlightIds", "displayAnnotations", "cliqueRelations", "containmentRelations", reasoning, "excludeSingletons", "relationProperties", "prefixProperties", "conditionalProperties", "nodeFilter")
);
