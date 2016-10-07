ace.define("ace/snippets/markdownish",["require","exports","module"], function(require, exports, module) {
"use strict";

var markdownSnippetText = require("ace/snippets/markdown").snippetText;
var shSnippetText = require("ace/snippets/sh").snippetText;

exports.snippetText = markdownSnippetText + shSnippetText;
exports.scope = "markdownish";

});

ace.define("ace/snippets/markdown",["require","exports","module"], function(require, exports, module) {
"use strict";

exports.snippetText = "# Markdown\n\
\n\
# Includes octopress (http://octopress.org/) snippets\n\
\n\
snippet [\n\
	[${1:text}](http://${2:address} \"${3:title}\")\n\
snippet [*\n\
	[${1:link}](${2:`@*`} \"${3:title}\")${4}\n\
\n\
snippet [:\n\
	[${1:id}]: http://${2:url} \"${3:title}\"\n\
snippet [:*\n\
	[${1:id}]: ${2:`@*`} \"${3:title}\"\n\
\n\
snippet ![\n\
	![${1:alttext}](${2:/images/image.jpg} \"${3:title}\")\n\
snippet ![*\n\
	![${1:alt}](${2:`@*`} \"${3:title}\")${4}\n\
\n\
snippet ![:\n\
	![${1:id}]: ${2:url} \"${3:title}\"\n\
snippet ![:*\n\
	![${1:id}]: ${2:`@*`} \"${3:title}\"\n\
\n\
snippet ===\n\
regex /^/=+/=*//\n\
	${PREV_LINE/./=/g}\n\
	\n\
	${0}\n\
snippet ---\n\
regex /^/-+/-*//\n\
	${PREV_LINE/./-/g}\n\
	\n\
	${0}\n\
snippet blockquote\n\
	{% blockquote %}\n\
	${1:quote}\n\
	{% endblockquote %}\n\
\n\
snippet blockquote-author\n\
	{% blockquote ${1:author}, ${2:title} %}\n\
	${3:quote}\n\
	{% endblockquote %}\n\
\n\
snippet blockquote-link\n\
	{% blockquote ${1:author} ${2:URL} ${3:link_text} %}\n\
	${4:quote}\n\
	{% endblockquote %}\n\
\n\
snippet bt-codeblock-short\n\
	```\n\
	${1:code_snippet}\n\
	```\n\
\n\
snippet bt-codeblock-full\n\
	``` ${1:language} ${2:title} ${3:URL} ${4:link_text}\n\
	${5:code_snippet}\n\
	```\n\
\n\
snippet codeblock-short\n\
	{% codeblock %}\n\
	${1:code_snippet}\n\
	{% endcodeblock %}\n\
\n\
snippet codeblock-full\n\
	{% codeblock ${1:title} lang:${2:language} ${3:URL} ${4:link_text} %}\n\
	${5:code_snippet}\n\
	{% endcodeblock %}\n\
\n\
snippet gist-full\n\
	{% gist ${1:gist_id} ${2:filename} %}\n\
\n\
snippet gist-short\n\
	{% gist ${1:gist_id} %}\n\
\n\
snippet img\n\
	{% img ${1:class} ${2:URL} ${3:width} ${4:height} ${5:title_text} ${6:alt_text} %}\n\
\n\
snippet youtube\n\
	{% youtube ${1:video_id} %}\n\
\n\
# The quote should appear only once in the text. It is inherently part of it.\n\
# See http://octopress.org/docs/plugins/pullquote/ for more info.\n\
\n\
snippet pullquote\n\
	{% pullquote %}\n\
	${1:text} {\" ${2:quote} \"} ${3:text}\n\
	{% endpullquote %}\n\
";
exports.scope = "markdown";

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

