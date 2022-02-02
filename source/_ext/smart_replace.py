import re
from textwrap import dedent

import requests
import yaml
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import nested_parse_with_titles


class SmartReplace(SphinxDirective):

    option_spec = {
        "source": directives.unchanged,
    }
    has_content = True

    def run(self):
        source = self.options["source"]
        # TODO: Some error checking.
        replacements = yaml.safe_load("\n".join(self.content))
        # TODO: Remove once you're done with this.
        #        full_content = dedent(
        #            """
        #            With a Title
        #            ------------
        #
        #
        #            .. note:: Something specific to Open edX you should know.
        #
        #                It's this.
        #
        #            """
        #        )
        full_content = requests.get(source).text
        full_content = full_content.lstrip("\n")

        for replacement in replacements:
            start_after = re.escape(replacement["start_after"])
            end_before = re.escape(replacement["end_before"])
            new_content = replacement["content"].strip()

            pattern = re.compile(f"({start_after}).*?({end_before})")
            full_content = re.sub(pattern, rf"\1{new_content}\2", full_content)

        full_content.strip()
        content_list = StringList(full_content.split("\n"))
        node = nodes.Element()
        nested_parse_with_titles(self.state, content_list, node)
        return node.children


def setup(app):

    app.add_directive("smart_replace", SmartReplace)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
