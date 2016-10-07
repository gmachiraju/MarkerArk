ace.define("ace/snippets/sqlish",["require","exports","module"], function(require, exports, module) {
"use strict";

var sqlSnippetText = require("ace/snippets/sql").snippetText;
var shSnippetText = require("ace/snippets/sh").snippetText;

exports.snippetText = sqlSnippetText + shSnippetText;
exports.scope = "sqlish";

});

ace.define("ace/snippets/sql",["require","exports","module"], function(require, exports, module) {
"use strict";

exports.snippetText = "snippet tbl\n\
	create table ${1:table} (\n\
		${2:columns}\n\
	);\n\
snippet col\n\
	${1:name}	${2:type}	${3:default ''}	${4:not null}\n\
snippet ccol\n\
	${1:name}	varchar2(${2:size})	${3:default ''}	${4:not null}\n\
snippet ncol\n\
	${1:name}	number	${3:default 0}	${4:not null}\n\
snippet dcol\n\
	${1:name}	date	${3:default sysdate}	${4:not null}\n\
snippet ind\n\
	create index ${3:$1_$2} on ${1:table}(${2:column});\n\
snippet uind\n\
	create unique index ${1:name} on ${2:table}(${3:column});\n\
snippet tblcom\n\
	comment on table ${1:table} is '${2:comment}';\n\
snippet colcom\n\
	comment on column ${1:table}.${2:column} is '${3:comment}';\n\
snippet addcol\n\
	alter table ${1:table} add (${2:column} ${3:type});\n\
snippet seq\n\
	create sequence ${1:name} start with ${2:1} increment by ${3:1} minvalue ${4:1};\n\
snippet s*\n\
	select * from ${1:table}\n\
";
exports.scope = "sql";

});

ace.define("ace/snippets/sh",["require","exports","module"], function(require, exports, module) {
"use strict";

exports.snippetText = "# Shebang. Executing bash via /usr/bin/env makes scripts more portable.\n\
snippet #!\n\
	#!/usr/bin/env bash\n\
	\n\
snippet if\n\
	if [[ ${1:condition} ]]; then\n\
		${2:#statements}\n\
	fi\n\
snippet elif\n\
	elif [[ ${1:condition} ]]; then\n\
		${2:#statements}\n\
snippet for\n\
	for (( ${2:i} = 0; $2 < ${1:count}; $2++ )); do\n\
		${3:#statements}\n\
	done\n\
snippet fori\n\
	for ${1:needle} in ${2:haystack} ; do\n\
		${3:#statements}\n\
	done\n\
snippet wh\n\
	while [[ ${1:condition} ]]; do\n\
		${2:#statements}\n\
	done\n\
snippet until\n\
	until [[ ${1:condition} ]]; do\n\
		${2:#statements}\n\
	done\n\
snippet case\n\
	case ${1:word} in\n\
		${2:pattern})\n\
			${3};;\n\
	esac\n\
snippet go \n\
	while getopts '${1:o}' ${2:opts} \n\
	do \n\
		case $$2 in\n\
		${3:o0})\n\
			${4:#staments};;\n\
		esac\n\
	done\n\
# Set SCRIPT_DIR variable to directory script is located.\n\
snippet sdir\n\
	SCRIPT_DIR=\"$( cd \"$( dirname \"${BASH_SOURCE[0]}\" )\" && pwd )\"\n\
# getopt\n\
snippet getopt\n\
	__ScriptVersion=\"${1:version}\"\n\
\n\
	#===  FUNCTION  ================================================================\n\
	#         NAME:  usage\n\
	#  DESCRIPTION:  Display usage information.\n\
	#===============================================================================\n\
	function usage ()\n\
	{\n\
			cat <<- EOT\n\
\n\
	  Usage :  $${0:0} [options] [--] \n\
\n\
	  Options: \n\
	  -h|help       Display this message\n\
	  -v|version    Display script version\n\
\n\
			EOT\n\
	}    # ----------  end of function usage  ----------\n\
\n\
	#-----------------------------------------------------------------------\n\
	#  Handle command line arguments\n\
	#-----------------------------------------------------------------------\n\
\n\
	while getopts \":hv\" opt\n\
	do\n\
	  case $opt in\n\
\n\
		h|help     )  usage; exit 0   ;;\n\
\n\
		v|version  )  echo \"$${0:0} -- Version $__ScriptVersion\"; exit 0   ;;\n\
\n\
		\\? )  echo -e \"\\n  Option does not exist : $OPTARG\\n\"\n\
			  usage; exit 1   ;;\n\
\n\
	  esac    # --- end of case ---\n\
	done\n\
	shift $(($OPTIND-1))\n\
\n\
";
exports.scope = "sh";

});

